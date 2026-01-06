import os
import sys
import subprocess
import time
import json
import shutil
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from config import PYTHON_DATASET_PATH, JAVA_DATASET_PATH, TEMP_PATH, GENERATED_CODE_PATH, TEST_MODEL_RESULTS, TEST_RESULTS

# ================= FLAGS TO CONFIGURE THE ANALYSIS =================
DEBUG = False  # if enabled, it will print the output of the Docker commands to stdout
MAX_WORKERS = 4
RUN_TESTS_ON_GENERATED_CODE = True
TEST_MODE = False # if True, only runs on a few samples for verification
# ========================== END OF FLAGS ===========================

STDOUT = sys.stdout if DEBUG else subprocess.DEVNULL
STDERR = subprocess.STDOUT if DEBUG else subprocess.DEVNULL

DOCKER_BIN = "/Applications/Docker.app/Contents/Resources/bin/docker"
if not os.path.exists(DOCKER_BIN):
    DOCKER_BIN = "docker"

def get_base_image_info(item_id, technique, source, is_python=True):
    """Find the base image name and Dockerfile for a given prompt ID, technique and source."""
    if is_python:
        parent_dir = os.path.join(PYTHON_DATASET_PATH, technique, source)
    else:
        parent_dir = os.path.join(JAVA_DATASET_PATH, "src", "main", "java", "com", "sallm", technique, source)
        
    dockerfile = os.path.join(parent_dir, f"{item_id}_Dockerfile")
    image_tag = f"sallm-{('py' if is_python else 'java')}-{item_id}".lower()
    
    return image_tag, dockerfile, parent_dir

def build_base_images(unique_prompts):
    """Build base images once."""
    unique_set = set(unique_prompts)
    if not unique_set: return
    print(f"Ensuring {len(unique_set)} base images exist...")
    for item_id, technique, source, is_python in tqdm(unique_set, desc="Checking/Building base images"):
        tag, df, context = get_base_image_info(item_id, technique, source, is_python)
        
        # Check if exists
        check = subprocess.run([DOCKER_BIN, "inspect", "--type=image", tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if check.returncode != 0:
            if not os.path.exists(df):
                if DEBUG: print(f"Warning: Dockerfile not found for {item_id} at {df}")
                continue
            subprocess.run([DOCKER_BIN, "build", "-t", tag, "-f", df, context], stdout=STDOUT, stderr=STDERR, check=True)

def parse_java_xml_reports(report_dir):
    """Parse Surefire XML reports and extract method-level results."""
    results = []
    if not os.path.exists(report_dir): return results
    
    for f in os.listdir(report_dir):
        if f.endswith(".xml") and f.startswith("TEST-"):
            try:
                tree = ET.parse(os.path.join(report_dir, f))
                root = tree.getroot()
                for testcase in root.findall("testcase"):
                    name = testcase.get("name")
                    # Check for failures or errors
                    failure = testcase.find("failure")
                    error = testcase.find("error")
                    status = "Failed" if (failure is not None or error is not None) else "Passed"
                    results.append((name, status))
            except Exception as e:
                if DEBUG: print(f"Error parsing XML {f}: {e}")
    return results

def process_single_file(file_info):
    """Run test for a single code file."""
    file_path, item_id, technique, source, lang, is_python = file_info
    parent_dir_name = os.path.basename(os.path.dirname(file_path))
    
    image_tag, _, _ = get_base_image_info(item_id, technique, source, is_python)
    
    # Restructured Output Filename
    if os.path.abspath(TEMP_PATH) in os.path.abspath(file_path):
        output_name = f"Model_{parent_dir_name}_{lang}_{technique}_{item_id}_results.csv"
        output_path = os.path.join(TEST_MODEL_RESULTS, output_name)
    else:
        output_name = f"Dataset_{lang}_{technique}_{item_id}_results.csv"
        output_path = os.path.join(TEST_RESULTS, output_name)
        
    if os.path.exists(output_path): return
    
    container_name = f"eval-{int(time.time()*1000)}-{os.getpid()}"
    
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        if is_python:
            run_cmd = [
                DOCKER_BIN, "run", "--name", container_name,
                "-v", f"{os.path.abspath(file_path)}:/prompt/{item_id}.py",
                image_tag
            ]
            subprocess.run(run_cmd, stdout=STDOUT, stderr=STDERR, timeout=90)
            res_in_cont = f"/prompt/test_{item_id}_results.csv"
            subprocess.run([DOCKER_BIN, "cp", f"{container_name}:{res_in_cont}", output_path], stdout=STDOUT, stderr=STDERR)
        else:
            rel_dir = f"com/sallm/{technique}/{source}"
            run_cmd = [
                DOCKER_BIN, "run", "--name", container_name,
                "-v", f"{os.path.abspath(file_path)}:/app/src/main/java/{rel_dir}/{item_id}.java",
                image_tag
            ]
            subprocess.run(run_cmd, stdout=STDOUT, stderr=STDERR, timeout=180)
            
            # Extract granular results for Java
            local_report_dir = os.path.join(TEMP_PATH, f"reports_{container_name}")
            os.makedirs(local_report_dir, exist_ok=True)
            subprocess.run([DOCKER_BIN, "cp", f"{container_name}:/app/target/surefire-reports/.", local_report_dir], stdout=STDOUT, stderr=STDERR)
            
            java_results = parse_java_xml_reports(local_report_dir)
            if java_results:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status\n")
                    for name, status in java_results:
                        f.write(f"{name},{status}\n")
            
            # Cleanup local reports
            shutil.rmtree(local_report_dir)
            
    except Exception as e:
        if DEBUG: print(f"Error {item_id}: {e}")
    finally:
        subprocess.run([DOCKER_BIN, "rm", "-f", container_name], stdout=STDOUT, stderr=STDERR)

def get_all_to_process(root_dir):
    """Scan directory for files and identify their metadata."""
    to_process = []
    unique_prompts = []
    
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith('.py') or f.endswith('.java'):
                item_id_file = os.path.splitext(f)[0]
                if not item_id_file.lower().startswith('test') and '_cwe' in item_id_file.lower():
                    is_python = f.endswith('.py')
                    lang = "Python" if is_python else "Java"
                    
                    if '__' in f:
                        # Extracted format: {technique}__{source}__{item_id}.ext
                        try:
                            technique, source, item_id = item_id_file.split('__', 2)
                        except:
                            continue
                    else:
                        # Dataset format: root/technique/source/id.ext
                        parts = root.split(os.sep)
                        try:
                            item_id = item_id_file
                            source = parts[-1]
                            technique = parts[-2]
                        except:
                            continue
                    
                    to_process.append((os.path.join(root, f), item_id, technique, source, lang, is_python))
                    unique_prompts.append((item_id, technique, source, is_python))
                    
    return to_process, unique_prompts

def save_generated_code(jsonl_folder, temp_folder):
    """Save code from JSONL files to temp folder for evaluation."""
    if not os.path.exists(jsonl_folder): return
    jsonl_files = sorted([f for f in os.listdir(jsonl_folder) if f.endswith('.jsonl')])
    if TEST_MODE: jsonl_files = jsonl_files[:1]

    for f_name in jsonl_files:
        with open(os.path.join(jsonl_folder, f_name), 'r', encoding='utf-8') as f:
            model_name = f_name.replace('.jsonl', '')
            for line in f:
                try:
                    d = json.loads(line)
                    technique = d.get('technique', 'Assertion')
                    source = d.get('source', 'Author')
                    item_id = d.get('id', 'unknown')
                    if item_id.endswith('.py') or item_id.endswith('.java'):
                        item_id = os.path.splitext(item_id)[0]
                    if item_id.startswith(f"{technique}_{source}_"):
                        item_id = item_id.replace(f"{technique}_{source}_", "")
                    
                    raw_output = d.get('output', [])
                    if isinstance(raw_output, dict) and 'choices' in raw_output:
                        outputs = raw_output['choices']
                    elif isinstance(raw_output, list):
                        outputs = raw_output
                    else:
                        outputs = [raw_output] if raw_output else []
                    
                    for idx, out in enumerate(outputs):
                        code = out.get('cleared_code', '')
                        if not code: continue
                        
                        ext = ".java" if "public class" in code else ".py"
                        target_dir = os.path.join(temp_folder, f"{model_name}_R{idx+1}")
                        os.makedirs(target_dir, exist_ok=True)
                        target_file = os.path.join(target_dir, f"{technique}__{source}__{item_id}{ext}")
                        with open(target_file, 'w', encoding='utf-8') as tf:
                            tf.write(code)
                except Exception as e:
                    pass

if __name__ == "__main__":
    if RUN_TESTS_ON_GENERATED_CODE:
        if os.path.exists(TEMP_PATH): shutil.rmtree(TEMP_PATH)
        os.makedirs(TEMP_PATH)
        print("Extracting code from JSONL files...")
        save_generated_code(GENERATED_CODE_PATH, TEMP_PATH)
        target_dir = TEMP_PATH
    else:
        repo_root = os.path.dirname(PYTHON_DATASET_PATH)
        target_dir = repo_root

    to_process, unique_prompts = get_all_to_process(target_dir)
    
    if TEST_MODE:
        py_files = [p for p in to_process if p[5]]
        jv_files = [p for p in to_process if not p[5]]
        # Pick a few from each for testing
        to_process = py_files[:1] + jv_files[:1] 
        print(f"TEST_MODE is ON: Processing {len(to_process)} samples.")
        needed_prompts = set((p[1], p[2], p[3], p[5]) for p in to_process)
        unique_prompts = list(needed_prompts)

    if not to_process:
        print("No files found to process.")
        sys.exit(0)

    # Build base images
    build_base_images(unique_prompts)
    
    # Run tests
    print(f"Executing {len(to_process)} tests...")
    start = time.time()
    workers = 1 if DEBUG else MAX_WORKERS
    with ProcessPoolExecutor(max_workers=workers) as executor:
        list(tqdm(executor.map(process_single_file, to_process), total=len(to_process), desc="Running Tests"))
        
    print(f"Finished in {(time.time() - start)/60:.2f} minutes.")
