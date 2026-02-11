import os
import sys
import subprocess
import time
import json
import shutil
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from config import PYTHON_DATASET_PATH, JAVA_DATASET_PATH, GITHUB_PYTHON_DATASET_PATH, GITHUB_JAVA_DATASET_PATH, TEMP_PATH, GENERATED_CODE_PATH, TEST_MODEL_RESULTS, TEST_RESULTS, TEST_FOLDER

# ================= FLAGS TO CONFIGURE THE ANALYSIS =================
DEBUG = False  # if enabled, it will print the output of the Docker commands to stdout
MAX_WORKERS = 4
RUN_TESTS_ON_GENERATED_CODE = True
TEST_MODE = False # if True, only runs on a few samples for verification
MODEL_FILTER = None  # Filter for specific model: 'gpt', 'gemini', 'qwen', 'starcoder', or None for all
LANG_FILTER = "Python"   # Filter for specific language: 'Python', 'Java', or None for all
TEMP_FILTER = None   # Filter for specific temperature: '0.0', '0.2', ..., '1.0', or None for all
ONLY_GITHUB = True   # If True, only runs on GitHub datasets (github-dataset_*.jsonl)
MAVEN_CACHE_PATH = os.path.join(JAVA_DATASET_PATH, ".m2_cache")
# ========================== END OF FLAGS ===========================



STDOUT = sys.stdout if DEBUG else subprocess.DEVNULL
STDERR = subprocess.STDOUT if DEBUG else subprocess.DEVNULL

# Handle Docker binary path for both macOS and Windows
DOCKER_BIN = shutil.which("docker")
if not DOCKER_BIN:
    if sys.platform == "darwin":  # macOS
        macos_docker = "/Applications/Docker.app/Contents/Resources/bin/docker"
        if os.path.exists(macos_docker):
            DOCKER_BIN = macos_docker
    if not DOCKER_BIN:
        DOCKER_BIN = "docker"

def fix_java_code(code, item_id, technique, source):
    """Ensure Java code has the correct class name and package."""
    # Ensure package declaration matches
    expected_package = f"com.sallm.{technique}.{source}"
    if f"package {expected_package};" not in code:
        # Remove existing package and add correct one
        code = re.sub(r'package\s+[\w\.]+;\s*', '', code)
        code = f"package {expected_package};\n\n" + code

    # Ensure class name matches item_id
    code = re.sub(r'public\s+class\s+\w+', f'public class {item_id}', code)
    
    return code

def warm_up_maven_cache():
    """Run maven on a sample pom.xml to warm up the cache sequentially."""
    sample_pom = os.path.join(JAVA_DATASET_PATH, "pom.xml")
    if not os.path.exists(sample_pom):
        # Find any pom.xml in the dataset
        for root, dirs, files in os.walk(os.path.join(JAVA_DATASET_PATH, "src")):
            if "pom.xml" in files:
                sample_pom = os.path.join(root, "pom.xml")
                break
    
    if os.path.exists(sample_pom):
        print(f"Warming up Maven cache using {sample_pom}...")
        os.makedirs(MAVEN_CACHE_PATH, exist_ok=True)
        repo_local = os.path.join(os.path.abspath(MAVEN_CACHE_PATH), "repository")
        # We use the host maven to populate the cache
        cmd = ["mvn", "dependency:go-offline", "-B", "-f", sample_pom, f"-Dmaven.repo.local={repo_local}"]
        subprocess.run(cmd, stdout=STDOUT, stderr=STDERR)
    else:
        print("Warning: No pom.xml found to warm up Maven cache.")

def get_base_image_info(item_id, technique, source, is_python=True):
    """Find the base image name and Dockerfile for a given prompt ID, technique and source."""
    if is_python:
        if source == "GitHubDataset":
            # Special case for GitHubDataset which is in the root
            parent_dir = os.path.join(GITHUB_PYTHON_DATASET_PATH, "GitHub")
        else:
            parent_dir = os.path.join(PYTHON_DATASET_PATH, technique, source)
        context = parent_dir
    else:
        if source == "GitHub":
            # Special case for GitHub Java dataset
            parent_dir = os.path.join(GITHUB_JAVA_DATASET_PATH, "src", "main", "java", "com", "sallm", "GitHub", "GitHub")
            context = GITHUB_JAVA_DATASET_PATH
        else:
            parent_dir = os.path.join(JAVA_DATASET_PATH, "src", "main", "java", "com", "sallm", technique, source)
            context = parent_dir
        
    dockerfile = os.path.join(parent_dir, f"{item_id}_Dockerfile")
    image_tag = f"sallm-{('py' if is_python else 'java')}-{item_id}".lower()
    if DEBUG: print(f"DEBUG: get_base_image_info: item_id={item_id}, source={source} -> image_tag={image_tag}, context={context}")
    
    return image_tag, dockerfile, context

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

def check_compilable_java(code):
    """
    Enhanced Java compilability check with multiple heuristics ported from filter_code.py.
    """
    if not code or len(code.strip()) < 20:
        return False

    # Check brace balance
    if code.count('{') != code.count('}'):
        return False

    # Check parenthesis balance
    if code.count('(') != code.count(')'):
        return False

    # Check bracket balance
    if code.count('[') != code.count(']'):
        return False

    # Must have a class definition
    if not re.search(r'\b(class|interface|enum)\s+\w+', code):
        return False

    # Check for incomplete statements (line ending without terminator mid-code)
    lines = code.split('\n')
    for i, line in enumerate(lines[:-5] if len(lines) > 5 else []):  # Check all but last 5 lines
        stripped = line.strip()
        if stripped and not stripped.startswith('//') and not stripped.startswith('/*') and not stripped.startswith('*'):
            # Should end with proper terminator or control character
            if re.search(r'[a-zA-Z0-9]$', stripped):
                if not (stripped.endswith(';') or stripped.endswith('{') or stripped.endswith('}') or stripped.endswith(',')):
                    # Could be continuation, check next line
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        # If next line doesn't continue the statement, this is likely truncated
                        if next_line and not next_line.startswith('.') and not next_line.startswith('['):
                            return False

    # Check for misplaced imports (should be at top)
    in_class = False
    for line in lines:
        stripped = line.strip()
        if re.match(r'(public\s+)?(abstract\s+)?(final\s+)?class\s+\w+', stripped):
            in_class = True
        if in_class and stripped.startswith('import '):
            return False  # Import inside class body

    # Check for duplicate class definitions
    class_count = len(re.findall(r'\b(public\s+)?class\s+\w+', code))
    if class_count > 1:
        return False

    return True

def process_single_file(file_info):
    """Run test for a single code file."""
    file_path, item_id, technique, source, lang, is_python = file_info
    parent_dir_name = os.path.basename(os.path.dirname(file_path))

    image_tag, _, _ = get_base_image_info(item_id, technique, source, is_python)

    # Restructured Output Filename
    if os.path.abspath(TEMP_PATH) in os.path.abspath(file_path):
        output_name = f"Model_{parent_dir_name}_{lang}_{technique}_{item_id}_results.csv"
    else:
        output_name = f"Dataset_{lang}_{technique}_{item_id}_results.csv"

    # Result Organization by Temperature
    temp_val = "unknown"
    # Try to extract temperature from parent_dir_name or filename
    # Use findall to take the last match, as model names (e.g. gemini-2.5) might contain decimals
    temp_matches = re.findall(r"(\d\.\d)", parent_dir_name)
    if not temp_matches:
        temp_matches = re.findall(r"(\d\.\d)", os.path.basename(file_path))

    if temp_matches:
        temp_val = temp_matches[-1]

    temp_dir = os.path.join(TEST_MODEL_RESULTS, f"temp_{temp_val}")
    output_path = os.path.join(temp_dir, output_name)

    if os.path.exists(output_path): return

    # Early validation for Java code - check compilability before running Docker
    if not is_python:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()

            if not check_compilable_java(code_content):
                # Code is not compilable, write error results directly
                os.makedirs(temp_dir, exist_ok=True)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                clean_error_msg = "Java code failed pre-validation checks (unbalanced braces/parens, missing class definition, or structural issues)"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    f.write(f"testFunctionality,Error,{clean_error_msg}\n")
                    f.write(f"testSecurity,Error,{clean_error_msg}\n")
                return
        except Exception as e:
            if DEBUG: print(f"Error reading file {file_path} for pre-validation: {e}")

    container_name = f"eval-{int(time.time()*1000)}-{os.getpid()}"

    try:
        os.makedirs(temp_dir, exist_ok=True)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Convert Windows paths to proper format for Docker on Windows
        abs_file_path = os.path.abspath(file_path)
        abs_output_path = os.path.abspath(output_path)
        
        if sys.platform == "win32":
            # Convert Windows paths for Docker (forward slashes and proper format)
            # For Windows, Docker Desktop can handle both C:\ and /c/ style paths
            abs_file_path = abs_file_path.replace("\\", "/")
            abs_output_path = abs_output_path.replace("\\", "/")
        
        # Normalize path for Docker volume mount (Windows fix)
        local_mount_path = os.path.abspath(file_path).replace("\\", "/")

        if is_python:
            run_cmd = [
                DOCKER_BIN, "run", "--name", container_name,
                "-v", f"{local_mount_path}:/prompt/{item_id}.py",
                image_tag
            ]
            if DEBUG: print(f"DEBUG: Executing command: {' '.join(run_cmd)}")
            completed_process = subprocess.run(run_cmd, capture_output=True, text=True, timeout=90)
            res_in_cont = f"/prompt/test_{item_id}_results.csv"
            if completed_process.returncode == 0:
                subprocess.run([DOCKER_BIN, "cp", f"{container_name}:{res_in_cont}", abs_output_path], stdout=STDOUT, stderr=STDERR)
            else:
                error_msg = completed_process.stderr or completed_process.stdout
                clean_error_msg = error_msg.replace(',', ';').replace('\n', ' ')
                with open(abs_output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    f.write(f"testFunctionality,Error,{clean_error_msg}\n")
                    f.write(f"testSecurity,Error,{clean_error_msg}\n")
        else:
            rel_dir = f"com/sallm/{technique}/{source}"
            # Ensure Maven cache exists
            os.makedirs(MAVEN_CACHE_PATH, exist_ok=True)
            abs_maven_cache = os.path.abspath(MAVEN_CACHE_PATH).replace("\\", "/")

            run_cmd = [
                DOCKER_BIN, "run", "--name", container_name,
                "-v", f"{local_mount_path}:/app/src/main/java/{rel_dir}/{item_id}.java",
                "-v", f"{abs_maven_cache}:/root/.m2",
                image_tag
            ]
            completed_process = subprocess.run(run_cmd, capture_output=True, text=True, timeout=180)
            
            # Extract granular results for Java
            local_report_dir = os.path.join(TEMP_PATH, f"reports_{container_name}".replace("/", "_").replace("\\", "_"))
            os.makedirs(local_report_dir, exist_ok=True)
            
            cp_process = subprocess.run([DOCKER_BIN, "cp", f"{container_name}:/app/target/surefire-reports/.", local_report_dir], capture_output=True, text=True)
            
            java_results = parse_java_xml_reports(local_report_dir)
            if java_results:
                with open(abs_output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    for name, status in java_results:
                        f.write(f"{name},{status},\n")
            else:
                # Fallback: if no results parsed, write Error status with captured output
                error_msg = completed_process.stderr or completed_process.stdout
                # If cp failed, it might be a compilation error
                if cp_process.returncode != 0 and not error_msg:
                    error_msg = cp_process.stderr
                
                clean_error_msg = error_msg.replace(',', ';').replace('\n', ' ')
                with open(abs_output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    f.write(f"testFunctionality,Error,{clean_error_msg}\n")
                    f.write(f"testSecurity,Error,{clean_error_msg}\n")
            
            # Cleanup local reports
            shutil.rmtree(local_report_dir)
            
    except Exception as e:
        if DEBUG: print(f"Error {item_id}: {e}")
        if not is_python:
            # Fallback for Java exceptions (e.g. Docker timeout or crash)
            try:
                with open(abs_output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status\n")
                    f.write("testFunctionality,Error\n")
                    f.write("testSecurity,Error\n")
            except:
                pass
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
    if not os.path.exists(jsonl_folder): 
        print(f"Error: JSONL folder not found: {jsonl_folder}")
        return
    
    jsonl_files = sorted([f for f in os.listdir(jsonl_folder) if f.endswith('.jsonl')])
    
    if TEST_MODE:
        # We process all model files but will limit samples per file
        print(f"TEST_MODE: Will pick 1 sample from each of the {len(jsonl_files)} files.")
    
    # Filter by model if specified
    if MODEL_FILTER:
        jsonl_files = [f for f in jsonl_files if MODEL_FILTER.lower() in f.lower()]
        print(f"MODEL_FILTER '{MODEL_FILTER}': Processing {len(jsonl_files)} files")

    # Filter by temperature if specified
    if TEMP_FILTER:
        jsonl_files = [f for f in jsonl_files if f"_{TEMP_FILTER}.jsonl" in f]
        print(f"TEMP_FILTER '{TEMP_FILTER}': Processing {len(jsonl_files)} files")

    # Add language filter for JSONL files
    if LANG_FILTER:
        if LANG_FILTER.lower() == 'java':
            jsonl_files = [f for f in jsonl_files if 'java' in f.lower()]
        elif LANG_FILTER.lower() == 'python':
            jsonl_files = [f for f in jsonl_files if 'java' not in f.lower()]
        print(f"LANG_FILTER '{LANG_FILTER}': Selective extraction from {len(jsonl_files)} files")


    # Filter for github-dataset_ files if flag is set
    if ONLY_GITHUB:
        jsonl_files = [f for f in jsonl_files if f.startswith('github-dataset_')]
        print(f"ONLY_GITHUB filter: Processing {len(jsonl_files)} files")

    for f_name in jsonl_files:
        with open(os.path.join(jsonl_folder, f_name), 'r', encoding='utf-8') as f:
            model_name = f_name.replace('.jsonl', '')
            for line_idx, line in enumerate(f):
                if TEST_MODE and line_idx >= 1:
                    break
                try:
                    d = json.loads(line)
                    technique = d.get('technique', 'Assertion')
                    source = d.get('source', 'Author')
                    
                    # Robust item_id and extension extraction from the 'id' field
                    original_id = d.get('id', 'unknown')
                    if not original_id or original_id == 'unknown':
                        continue
                        
                    ext = os.path.splitext(original_id)[1]
                    item_id_no_ext = os.path.splitext(original_id)[0]
                    
                    # Clean technique_source prefix if present
                    item_id = item_id_no_ext
                    prefix = f"{technique}_{source}_"
                    if item_id.startswith(prefix):
                        item_id = item_id[len(prefix):]
                    
                    # Handle 'generations' dict from filter_code.py output
                    generations = d.get('generations', {})
                    if generations:
                        for lang_key, code_list in generations.items():
                            for idx, code_obj in enumerate(code_list):
                                code = code_obj.get('cleared_code', '')
                                if TEST_MODE and (lang_key != 'English' or idx >= 1):
                                    continue
                                
                                code = code_obj.get('cleared_code', '')
                                if not code: continue
                                
                                if lang_key == 'Java' or (lang_key == 'English' and ext == '.java'):
                                    code = fix_java_code(code, item_id, technique, source)

                                # Inject language name into the folder name to make it unique
                                if '_' in model_name:
                                    parts = model_name.rsplit('_', 1)
                                    dir_name = f"{parts[0]}_{lang_key}_{parts[1]}"
                                else:
                                    dir_name = f"{model_name}_{lang_key}"
                                
                                target_dir = os.path.join(temp_folder, f"{dir_name}_R{idx+1}")
                                os.makedirs(target_dir, exist_ok=True)
                                target_file = os.path.join(target_dir, f"{technique}__{source}__{item_id}{ext}")
                                with open(target_file, 'w', encoding='utf-8') as tf:
                                    tf.write(code)
                    else:
                        # Legacy 'output' handling
                        outputs = d.get('output', [])
                        if not isinstance(outputs, list):
                            outputs = [outputs]
                        
                        for idx, out in enumerate(outputs):
                            if TEST_MODE and idx >= 1:
                                break
                            if isinstance(out, dict):
                                code = out.get('cleared_code', '')
                            else:
                                code = out # fallback
                                
                            if not code: continue
                            
                            if ext == '.java':
                                code = fix_java_code(code, item_id, technique, source)

                            target_dir = os.path.join(temp_folder, f"{model_name}_R{idx+1}")
                            os.makedirs(target_dir, exist_ok=True)
                            target_file = os.path.join(target_dir, f"{technique}__{source}__{item_id}{ext}")
                            with open(target_file, 'w', encoding='utf-8') as tf:
                                tf.write(code)
                except Exception as e:
                    if DEBUG: print(f"Error processing line in {f_name}: {e}")


if __name__ == "__main__":
    # Folder management: clean up and create required directories
    if os.path.exists(TEMP_PATH): 
        print(f"Removing existing temp folder: {TEMP_PATH}")
        shutil.rmtree(TEMP_PATH)
    os.makedirs(TEMP_PATH, exist_ok=True)
    print(f"Created temp folder: {TEMP_PATH}")
    
    # Ensure results directories exist
    os.makedirs(TEST_MODEL_RESULTS, exist_ok=True)
    print(f"Created TEST_MODEL_RESULTS folder: {TEST_MODEL_RESULTS}")
    
    os.makedirs(TEST_RESULTS, exist_ok=True)
    print(f"Created TEST_RESULTS folder: {TEST_RESULTS}")
    
    # Create test folder
    os.makedirs(TEST_FOLDER, exist_ok=True)
    print(f"Created test folder: {TEST_FOLDER}")

    # Warm up Maven cache if Java is involved
    if LANG_FILTER is None or LANG_FILTER.lower() == 'java':
        warm_up_maven_cache()

    if RUN_TESTS_ON_GENERATED_CODE:
        print(f"Extracting code from JSONL files in: {GENERATED_CODE_PATH}")
        save_generated_code(GENERATED_CODE_PATH, TEMP_PATH)
        target_dir = TEMP_PATH

    else:
        target_dir = JAVA_DATASET_PATH

    to_process, unique_prompts = get_all_to_process(target_dir)
    
    # Apply MODEL_FILTER
    if MODEL_FILTER:
        print(f"MODEL_FILTER '{MODEL_FILTER}': Filtering samples...")
        to_process = [p for p in to_process if MODEL_FILTER.lower() in p[0].lower()]  # p[0] is file_path
        needed_prompts = set((p[1], p[2], p[3], p[5]) for p in to_process)
        unique_prompts = list(needed_prompts)

    # Filter by Language if specified
    if LANG_FILTER:
        print(f"LANG_FILTER '{LANG_FILTER}': Filtering samples...")
        to_process = [p for p in to_process if LANG_FILTER.lower() in p[4].lower()]
        needed_prompts = set((p[1], p[2], p[3], p[5]) for p in to_process)
        unique_prompts = list(needed_prompts)

    if TEST_MODE:
        # Since we already limited extraction in save_generated_code,
        # we can just use all discovered files.
        print(f"TEST_MODE is ON: Processing {len(to_process)} samples from all models.")
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
