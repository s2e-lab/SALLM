import os
import sys
import subprocess
import time
import json
import shutil
import re
import ast
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from config import PYTHON_DATASET_PATH, JAVA_DATASET_PATH, GITHUB_PYTHON_DATASET_PATH, GITHUB_JAVA_DATASET_PATH, CPP_DATASET_PATH, GENERATED_CODE_PATH, TEST_RESULTS, TEST_FOLDER, SIF_DIR, BASE_DIR

# Add parent directory to path to import from Generation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Generation'))
from filter_code import strip_starcoder_tokens, fix_truncated_java, extract_code_block

# ================= FLAGS TO CONFIGURE THE ANALYSIS =================
DEBUG = False  # if enabled, it will print the output of the Singularity commands to stdout
MAX_WORKERS = 32
RUN_TESTS_ON_GENERATED_CODE = True
TEST_MODE = False   # if True, only runs on a few samples for verification
MODEL_FILTER = "gpt"  # Filter for specific model: 'gpt', 'gemini', 'qwen', 'starcoder', or None for all
LANG_FILTER = "cpp"  # Filter for specific language: 'Python', 'Java', 'cpp', or None for all
TEMP_FILTER = None   # Filter for specific temperature: '0.0', '0.2', ..., '1.0', or None for all
ONLY_GITHUB = False  # If True, only runs on GitHub datasets (github-dataset_*.jsonl)
MAVEN_CACHE_PATH = os.path.join(JAVA_DATASET_PATH, ".m2_cache")
# C++ GoogleTest prebuilt paths (from DatasetCPP/build)
CPP_BUILD_DIR     = os.path.join(CPP_DATASET_PATH, "build")
GTEST_INCLUDE     = os.path.join(CPP_BUILD_DIR, "_deps", "googletest-src", "googletest", "include")
GTEST_LIB         = os.path.join(CPP_BUILD_DIR, "lib", "libgtest.a")
GTEST_MAIN_LIB    = os.path.join(CPP_BUILD_DIR, "lib", "libgtest_main.a")
# ========================== END OF FLAGS ===========================

# ---------------------------------------------------------------------------
# Derive TEMP_PATH and TEST_MODEL_RESULTS from the flags above so that
# different (ONLY_GITHUB, LANG_FILTER, MODEL_FILTER) combinations write to
# isolated folders — safe for parallel jobs.
#
# TEMP naming:   temp[_{model}][_github][_{lang}]
#   e.g.  MODEL_FILTER="gemini", ONLY_GITHUB=True,  LANG_FILTER="Java"
#         → temp_gemini_github_java
#
# RESULTS naming: TestModelsResults[_GitHub][_{Lang}]
#   e.g.  ONLY_GITHUB=True,  LANG_FILTER="Java"  → TestModelsResults_GitHub_Java
#         ONLY_GITHUB=False, LANG_FILTER="Python" → TestModelsResults_Python
#         ONLY_GITHUB=False, LANG_FILTER=None     → TestModelsResults
# ---------------------------------------------------------------------------
def _compute_paths(model_filter, only_github, lang_filter):
    temp_parts = []
    if model_filter:
        temp_parts.append(model_filter.lower())
    if only_github:
        temp_parts.append("github")
    if lang_filter:
        temp_parts.append(lang_filter.lower())
    temp_suffix = ("_" + "_".join(temp_parts)) if temp_parts else ""
    temp_path = os.path.join(BASE_DIR, f"temp{temp_suffix}")

    res_parts = []
    if only_github:
        res_parts.append("GitHub")
    if lang_filter:
        res_parts.append(lang_filter.capitalize())
    results_dir = os.path.join(
        BASE_DIR,
        "TestModelsResults" + (("_" + "_".join(res_parts)) if res_parts else ""),
    )
    return temp_path, results_dir

TEMP_PATH, TEST_MODEL_RESULTS = _compute_paths(MODEL_FILTER, ONLY_GITHUB, LANG_FILTER)


STDOUT = sys.stdout if DEBUG else subprocess.DEVNULL
STDERR = subprocess.STDOUT if DEBUG else subprocess.DEVNULL

# Find apptainer or singularity binary
APPTAINER_BIN = shutil.which("apptainer") or shutil.which("singularity")
if not APPTAINER_BIN:
    print("Error: Neither 'apptainer' nor 'singularity' found in PATH.")
    sys.exit(1)


def _camel_to_snake(name):
    """Convert camelCase or PascalCase to snake_case."""
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
    return s.lower()


def _get_expected_method_names(item_id, technique, source):
    """Return the set of snake_case method names the test file calls on the generated class."""
    # Try GitHub Java dataset first, then standard Java dataset
    for dataset_path in (GITHUB_JAVA_DATASET_PATH, JAVA_DATASET_PATH):
        test_path = os.path.join(
            dataset_path, "src", "test", "java", "com", "sallm", technique, source,
            f"Test{item_id}.java",
        )
        if os.path.exists(test_path):
            break
    if not os.path.exists(test_path):
        return set()
    try:
        with open(test_path, encoding="utf-8") as f:
            content = f.read()
        # Find calls: instance.someMethod( or instance.some_method(
        return set(re.findall(r'instance\.([a-z][A-Za-z0-9_]*)\s*\(', content))
    except Exception:
        return set()


def _extract_public_methods(code):
    """Extract public non-constructor method names (lowercase start) from Java code."""
    # Match on a single line to avoid spanning into Javadoc comments.
    # Pattern: optional indent, public, optional static/final, return type, method name, (
    matches = re.findall(
        r'^\s*public\s+(?:static\s+)?(?:final\s+)?[\w<>\[\],\s]+?\s+([a-z]\w*)\s*\(',
        code, re.MULTILINE
    )
    excluded = {'main', 'toString', 'hashCode', 'equals'}
    return [m for m in matches if m not in excluded]

def fix_java_code(code, item_id, technique, source):
    """Ensure Java code has the correct class name, package, and method names."""
    # Robust cleaning and reconstruction
    code = strip_starcoder_tokens(code)
    code = fix_truncated_java(code)
    
    expected_package = f"com.sallm.{technique}.{source}"
    if f"package {expected_package};" not in code:
        code = re.sub(r'package\s+[\w\.]+;\s*', '', code)
        code = f"package {expected_package};\n\n" + code

    code = re.sub(r'public\s+class\s+\w+', f'public class {item_id}', code)

    # Rename methods to match what the test file expects.
    expected_names = _get_expected_method_names(item_id, technique, source)
    if not expected_names:
        return code

    for expected in sorted(expected_names):
        # 1. Already present — nothing to do.
        if re.search(r'\b' + re.escape(expected) + r'\b', code):
            continue

        # 2. Try the camelCase variant (e.g., match_string → matchString).
        camel = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), expected)
        if camel != expected and re.search(r'\b' + re.escape(camel) + r'\b', code):
            code = re.sub(r'\b' + re.escape(camel) + r'\b', expected, code)
            continue

        # 3. Fall back: rename the first public method not already in expected_names.
        for actual in _extract_public_methods(code):
            if actual not in expected_names:
                code = re.sub(r'\b' + re.escape(actual) + r'\b', expected, code)
                break

    return code


def warm_up_maven_cache():
    """Populate MAVEN_CACHE_PATH with Maven dependencies.

    Strategy (in order):
      1. Already populated → skip.
      2. Extract from the pre-built Java base SIF (no host Maven needed).
      3. Fall back to running host `mvn dependency:go-offline`.
    """
    os.makedirs(MAVEN_CACHE_PATH, exist_ok=True)
    abs_cache = os.path.abspath(MAVEN_CACHE_PATH)

    # Already populated?
    if os.path.isdir(os.path.join(abs_cache, "repository")):
        print(f"Maven cache already populated at {abs_cache}")
        return

    # Try extracting from the pre-built Java base SIF (deps are at /app/.m2 inside it)
    java_base_sif = os.path.join(SIF_DIR, "sallm-java-base.sif")
    if os.path.exists(java_base_sif):
        print(f"Extracting Maven deps from {java_base_sif} → {abs_cache} ...")
        result = subprocess.run(
            [APPTAINER_BIN, "exec", java_base_sif,
             "cp", "-r", "/app/.m2/.", abs_cache],
            capture_output=True, text=True,
        )
        if result.returncode == 0 and os.path.isdir(os.path.join(abs_cache, "repository")):
            print("Maven cache extracted successfully.")
            return
        print(f"Warning: SIF extraction had issues: {result.stderr[:200]}")

    # Fall back to host mvn
    mvn_bin = shutil.which("mvn")
    if not mvn_bin:
        print("Warning: 'mvn' not found in PATH and SIF extraction failed.")
        print("  Maven containers will download deps on first run (~1-2 min each).")
        return

    sample_pom = os.path.join(JAVA_DATASET_PATH, "pom.xml")
    if not os.path.exists(sample_pom):
        for root, dirs, files in os.walk(os.path.join(JAVA_DATASET_PATH, "src")):
            if "pom.xml" in files:
                sample_pom = os.path.join(root, "pom.xml")
                break

    if os.path.exists(sample_pom):
        print(f"Warming up Maven cache using {sample_pom}...")
        repo_local = os.path.join(abs_cache, "repository")
        cmd = [mvn_bin, "dependency:go-offline", "-B", "-f", sample_pom,
               f"-Dmaven.repo.local={repo_local}"]
        subprocess.run(cmd, stdout=STDOUT, stderr=STDERR)
    else:
        print("Warning: No pom.xml found for Maven warm-up.")


def get_sif_path(item_id, is_python=True, technique=None):
    """Return the path to the pre-built SIF image for a given item_id.

    For standard Java (non-GitHub), SIF names include the technique prefix to
    avoid collisions between items with the same item_id across techniques.
    GitHub Java items keep the original naming (no technique prefix).
    """
    if is_python:
        sif_name = f"sallm-py-{item_id}.sif".lower()
    elif technique and technique.lower() != "github":
        # Standard Java: technique-prefixed name
        sif_name = f"sallm-java-{technique}-{item_id}.sif".lower()
    else:
        # GitHub Java (or unknown): original naming
        sif_name = f"sallm-java-{item_id}.sif".lower()
    return os.path.join(SIF_DIR, sif_name)


def get_cpp_test_path(item_id, technique):
    """Return the path to the GoogleTest file for a C++ item."""
    test_file = f"test_{item_id}.cpp"
    return os.path.join(CPP_DATASET_PATH, "test", technique, test_file)


def run_cpp_test(file_path, item_id, technique, source, output_path, temp_dir):
    """Compile and run a C++ GoogleTest for a single generated file."""
    import tempfile
    test_src = get_cpp_test_path(item_id, technique)
    if not os.path.exists(test_src):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write("test,status,error_reason\n")
            f.write(f"testFunctionality,Error,Test file not found: {os.path.basename(test_src)}\n")
            f.write(f"testSecurity,Error,Test file not found: {os.path.basename(test_src)}\n")
        return

    # Build a temp dir mirroring src/technique/item_id.cpp so the test's
    # relative #include "../src/technique/item_id.cpp" resolves correctly.
    work_dir = os.path.join(temp_dir, f"cpp_{item_id}_{os.getpid()}")
    src_dir  = os.path.join(work_dir, "src", technique)
    test_dir = os.path.join(work_dir, "test", technique)
    os.makedirs(src_dir,  exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    shutil.copy2(file_path, os.path.join(src_dir, f"{item_id}.cpp"))
    shutil.copy2(test_src,  os.path.join(test_dir, f"test_{item_id}.cpp"))

    bin_path     = os.path.join(work_dir, "runTest")
    xml_path     = os.path.join(work_dir, "results.xml")
    test_cpp     = os.path.join(test_dir, f"test_{item_id}.cpp")

    compile_cmd = [
        "g++", "-std=c++17",
        f"-I{work_dir}",
        f"-I{GTEST_INCLUDE}",
        test_cpp,
        GTEST_LIB, GTEST_MAIN_LIB,
        "-lpthread",
        "-o", bin_path,
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        compile_result = subprocess.run(
            compile_cmd, capture_output=True, text=True, timeout=60
        )
        if compile_result.returncode != 0:
            err = compile_result.stderr.replace(',', ';').replace('\n', ' ')[:300]
            with open(output_path, 'w') as f:
                f.write("test,status,error_reason\n")
                f.write(f"testFunctionality,Error,Compilation failed: {err}\n")
                f.write(f"testSecurity,Error,Compilation failed: {err}\n")
            return

        run_result = subprocess.run(
            [bin_path, f"--gtest_output=xml:{xml_path}"],
            capture_output=True, text=True, timeout=60
        )

        # Parse GoogleTest XML
        results = []
        if os.path.exists(xml_path):
            try:
                tree = ET.parse(xml_path)
                for testcase in tree.getroot().iter("testcase"):
                    name   = testcase.get("name", "unknown")
                    failed = testcase.find("failure") is not None or testcase.find("error") is not None
                    results.append((name, "Failed" if failed else "Passed"))
            except Exception:
                pass

        if results:
            with open(output_path, 'w') as f:
                f.write("test,status,error_reason\n")
                for name, status in results:
                    f.write(f"{name},{status},\n")
        else:
            err = (run_result.stderr or run_result.stdout).replace(',', ';').replace('\n', ' ')[:300]
            with open(output_path, 'w') as f:
                f.write("test,status,error_reason\n")
                f.write(f"testFunctionality,Error,{err}\n")
                f.write(f"testSecurity,Error,{err}\n")

    except subprocess.TimeoutExpired:
        with open(output_path, 'w') as f:
            f.write("test,status,error_reason\n")
            f.write("testFunctionality,Error,Compile/run timed out\n")
            f.write("testSecurity,Error,Compile/run timed out\n")
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


def get_base_image_info(item_id, technique, source, is_python=True):
    """Find the base image name and Dockerfile for a given prompt ID, technique and source."""
    if is_python:
        if source == "GitHubDataset":
            parent_dir = os.path.join(GITHUB_PYTHON_DATASET_PATH, "GitHub")
        else:
            parent_dir = os.path.join(PYTHON_DATASET_PATH, technique, source)
        context = parent_dir
    else:
        if source == "GitHub":
            parent_dir = os.path.join(GITHUB_JAVA_DATASET_PATH, "src", "main", "java", "com", "sallm", "GitHub", "GitHub")
            context = GITHUB_JAVA_DATASET_PATH
        else:
            parent_dir = os.path.join(JAVA_DATASET_PATH, "src", "main", "java", "com", "sallm", technique, source)
            context = parent_dir

    dockerfile = os.path.join(parent_dir, f"{item_id}_Dockerfile")
    image_tag = f"sallm-{('py' if is_python else 'java')}-{item_id}".lower()
    if DEBUG:
        print(f"DEBUG: get_base_image_info: item_id={item_id}, source={source} -> image_tag={image_tag}, context={context}")

    return image_tag, dockerfile, context


def build_base_images(unique_prompts):
    """
    Ensure SIF images exist for all prompts.

    If Docker is available, builds missing Docker images then converts to SIF.
    Otherwise, checks that pre-built SIF files exist in SIF_DIR and warns about missing ones.
    """
    os.makedirs(SIF_DIR, exist_ok=True)
    unique_set = set(unique_prompts)
    if not unique_set:
        return

    docker_bin = shutil.which("docker")
    missing_sifs = []

    print(f"Checking {len(unique_set)} SIF images in {SIF_DIR} ...")
    for item_id, technique, source, is_python in tqdm(unique_set, desc="Checking SIF images"):
        sif_path = get_sif_path(item_id, is_python, technique)
        if os.path.exists(sif_path):
            continue

        if docker_bin:
            # Build Docker image then convert to SIF
            image_tag, df, context = get_base_image_info(item_id, technique, source, is_python)
            if not os.path.exists(df):
                if DEBUG:
                    print(f"Warning: Dockerfile not found for {item_id} at {df}")
                missing_sifs.append(sif_path)
                continue

            if DEBUG:
                print(f"Building Docker image {image_tag} from {df} ...")
            build_result = subprocess.run(
                [docker_bin, "build", "-t", image_tag, "-f", df, context],
                stdout=STDOUT, stderr=STDERR
            )
            if build_result.returncode != 0:
                print(f"Warning: Docker build failed for {item_id}")
                missing_sifs.append(sif_path)
                continue

            if DEBUG:
                print(f"Converting {image_tag} to {sif_path} ...")
            conv_result = subprocess.run(
                [APPTAINER_BIN, "build", sif_path, f"docker-daemon://{image_tag}"],
                stdout=STDOUT, stderr=STDERR
            )
            if conv_result.returncode != 0:
                print(f"Warning: Apptainer build failed for {item_id}")
                missing_sifs.append(sif_path)
        else:
            missing_sifs.append(sif_path)

    if missing_sifs:
        print(f"\nWARNING: {len(missing_sifs)} SIF image(s) are missing.")
        print("To build them, on a machine with Docker and Apptainer run:")
        print("  python build_sif_images.py")
        print("Then transfer the .sif files to:", SIF_DIR)
        print("Missing SIF files:")
        for p in missing_sifs[:10]:
            print(f"  {p}")
        if len(missing_sifs) > 10:
            print(f"  ... and {len(missing_sifs) - 10} more")


def parse_java_xml_reports(report_dir):
    """Parse Surefire XML reports and extract method-level results."""
    results = []
    if not os.path.exists(report_dir):
        return results

    for f in os.listdir(report_dir):
        if f.endswith(".xml") and f.startswith("TEST-"):
            try:
                tree = ET.parse(os.path.join(report_dir, f))
                root = tree.getroot()
                for testcase in root.findall("testcase"):
                    name = testcase.get("name")
                    failure = testcase.find("failure")
                    error = testcase.find("error")
                    status = "Failed" if (failure is not None or error is not None) else "Passed"
                    results.append((name, status))
            except Exception as e:
                if DEBUG:
                    print(f"Error parsing XML {f}: {e}")
    return results


def check_compilable_java(code):
    """Enhanced Java compilability check with multiple heuristics."""
    if not code or len(code.strip()) < 20:
        return False
    if code.count('{') != code.count('}'):
        return False
    if code.count('(') != code.count(')'):
        return False
    if code.count('[') != code.count(']'):
        return False
    if not re.search(r'\b(class|interface|enum)\s+\w+', code):
        return False

    lines = code.split('\n')
    for i, line in enumerate(lines[:-5] if len(lines) > 5 else []):
        stripped = line.strip()
        if stripped and not stripped.startswith('//') and not stripped.startswith('/*') and not stripped.startswith('*'):
            if re.search(r'[a-zA-Z0-9]$', stripped):
                if not (stripped.endswith(';') or stripped.endswith('{') or stripped.endswith('}') or stripped.endswith(',')):
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if next_line and not next_line.startswith('.') and not next_line.startswith('['):
                            return False

    in_class = False
    for line in lines:
        stripped = line.strip()
        if re.match(r'(public\s+)?(abstract\s+)?(final\s+)?class\s+\w+', stripped):
            in_class = True
        if in_class and stripped.startswith('import '):
            return False

    class_count = len(re.findall(r'\b(public\s+)?class\s+\w+', code))
    if class_count > 1:
        return False

    return True


def process_single_file(file_info):
    """Run test for a single code file using Apptainer/Singularity (or g++ for C++)."""
    file_path, item_id, technique, source, lang, is_python = file_info
    is_cpp = (lang == "C++")
    parent_dir_name = os.path.basename(os.path.dirname(file_path))

    sif_path = get_sif_path(item_id, is_python, technique)

    # Restructured Output Filename
    if os.path.abspath(TEMP_PATH) in os.path.abspath(file_path):
        output_name = f"Model_{parent_dir_name}_{lang}_{technique}_{item_id}_results.csv"
    else:
        output_name = f"Dataset_{lang}_{technique}_{item_id}_results.csv"

    # Result Organization by Temperature
    temp_val = "unknown"
    temp_matches = re.findall(r"(\d\.\d)", parent_dir_name)
    if not temp_matches:
        temp_matches = re.findall(r"(\d\.\d)", os.path.basename(file_path))
    if temp_matches:
        temp_val = temp_matches[-1]

    temp_dir = os.path.join(TEST_MODEL_RESULTS, f"temp_{temp_val}")
    output_path = os.path.join(temp_dir, output_name)

    if os.path.exists(output_path):
        return

    # C++ — compile and run directly with g++, no SIF needed
    if is_cpp:
        run_cpp_test(file_path, item_id, technique, source, output_path, TEMP_PATH)
        return

    # Early validation before running container
    if is_python:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
            try:
                ast.parse(code_content)
            except SyntaxError as e:
                os.makedirs(temp_dir, exist_ok=True)
                clean_error_msg = f"Python code failed parsing: {e.msg} at line {e.lineno}".replace(',', ';')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    f.write(f"testFunctionality,Error,{clean_error_msg}\n")
                    f.write(f"testSecurity,Error,{clean_error_msg}\n")
                return
        except Exception as e:
            if DEBUG:
                print(f"Error reading file {file_path} for pre-validation: {e}")
    else:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
            if not check_compilable_java(code_content):
                os.makedirs(temp_dir, exist_ok=True)
                clean_error_msg = "Java code failed pre-validation checks (unbalanced braces/parens, missing class definition, or structural issues)"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    f.write(f"testFunctionality,Error,{clean_error_msg}\n")
                    f.write(f"testSecurity,Error,{clean_error_msg}\n")
                return
        except Exception as e:
            if DEBUG:
                print(f"Error reading file {file_path} for pre-validation: {e}")

    # Check SIF image exists
    if not os.path.exists(sif_path):
        if DEBUG:
            print(f"Warning: SIF image not found: {sif_path}, skipping {item_id}")
        os.makedirs(temp_dir, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("test,status,error_reason\n")
            f.write(f"testFunctionality,Error,SIF image not found: {os.path.basename(sif_path)}\n")
            f.write(f"testSecurity,Error,SIF image not found: {os.path.basename(sif_path)}\n")
        return

    abs_file_path = os.path.abspath(file_path)

    try:
        os.makedirs(temp_dir, exist_ok=True)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if is_python:
            # The container runs in /prompt/ and writes test_{item_id}_results.csv there.
            # We bind:
            #   - the generated code file → /prompt/{item_id}.py   (replaces baked-in original)
            #   - the pre-created output file → /prompt/test_{item_id}_results.csv  (so writes reach the host)
            result_in_container = f"/prompt/test_{item_id}_results.csv"

            # Pre-create the output file so Apptainer can bind-mount it
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("")

            run_cmd = [
                APPTAINER_BIN, "run",
                "--bind", f"{abs_file_path}:/prompt/{item_id}.py",
                "--bind", f"{os.path.abspath(output_path)}:{result_in_container}",
                sif_path,
            ]
            completed_process = subprocess.run(
                run_cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=90,
            )

            if completed_process.returncode != 0 or os.path.getsize(output_path) == 0:
                error_msg = completed_process.stderr or completed_process.stdout
                clean_error_msg = error_msg.replace(',', ';').replace('\n', ' ')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    f.write(f"testFunctionality,Error,{clean_error_msg}\n")
                    f.write(f"testSecurity,Error,{clean_error_msg}\n")

        else:
            # Java: bind the generated .java file and the Maven cache.
            # Bind a local reports dir to /app/target/surefire-reports/ so XML reports
            # are written directly to the host (no docker cp needed).
            rel_dir = f"com/sallm/{technique}/{source}"
            os.makedirs(MAVEN_CACHE_PATH, exist_ok=True)
            abs_maven_cache = os.path.abspath(MAVEN_CACHE_PATH)

            # Bind all of /app/target as writable so Maven can create target/classes,
            # target/test-classes, and target/surefire-reports inside the container.
            local_target_dir = os.path.join(
                TEMP_PATH,
                f"target_{int(time.time()*1000)}_{os.getpid()}_{item_id}"
            )
            local_report_dir = os.path.join(local_target_dir, "surefire-reports")
            os.makedirs(local_report_dir, exist_ok=True)

            run_cmd = [
                APPTAINER_BIN, "run",
                "--bind", f"{abs_file_path}:/app/src/main/java/{rel_dir}/{item_id}.java",
                # Bind writable host cache over /app/.m2 so Maven can write .lastUpdated
                # files. The SIF runscript uses -Dmaven.repo.local=/app/.m2.
                "--bind", f"{abs_maven_cache}:/app/.m2",
                # Bind entire /app/target so Maven can write classes and test-classes too.
                "--bind", f"{local_target_dir}:/app/target",
                sif_path,
            ]
            completed_process = subprocess.run(
                run_cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=180,
            )

            java_results = parse_java_xml_reports(local_report_dir)
            if java_results:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    for name, status in java_results:
                        f.write(f"{name},{status},\n")
            else:
                error_msg = completed_process.stderr or completed_process.stdout
                clean_error_msg = error_msg.replace(',', ';').replace('\n', ' ')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("test,status,error_reason\n")
                    f.write(f"testFunctionality,Error,{clean_error_msg}\n")
                    f.write(f"testSecurity,Error,{clean_error_msg}\n")

            shutil.rmtree(local_target_dir, ignore_errors=True)

    except subprocess.TimeoutExpired:
        if DEBUG:
            print(f"Timeout for {item_id}")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("test,status,error_reason\n")
            f.write(f"testFunctionality,Error,Container timed out\n")
            f.write(f"testSecurity,Error,Container timed out\n")
    except Exception as e:
        if DEBUG:
            print(f"Error {item_id}: {e}")
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("test,status,error_reason\n")
                f.write(f"testFunctionality,Error,{str(e).replace(',', ';')}\n")
                f.write(f"testSecurity,Error,{str(e).replace(',', ';')}\n")
        except Exception:
            pass
    # No docker rm needed — Singularity/Apptainer runs are ephemeral


def get_all_to_process(root_dir):
    """Scan directory for files and identify their metadata."""
    to_process = []
    unique_prompts = []

    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.endswith('.py') or f.endswith('.java') or f.endswith('.cpp'):
                item_id_file = os.path.splitext(f)[0]
                if not item_id_file.lower().startswith('test') and '_cwe' in item_id_file.lower():
                    is_python = f.endswith('.py')
                    is_cpp = f.endswith('.cpp')
                    lang = "Python" if is_python else ("C++" if is_cpp else "Java")

                    if '__' in f:
                        try:
                            technique, source, item_id = item_id_file.split('__', 2)
                        except Exception:
                            continue
                    else:
                        parts = root.split(os.sep)
                        try:
                            item_id = item_id_file
                            source = parts[-1]
                            technique = parts[-2]
                        except Exception:
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
        print(f"TEST_MODE: Will pick 1 sample from each of the {len(jsonl_files)} files.")

    if MODEL_FILTER:
        jsonl_files = [f for f in jsonl_files if MODEL_FILTER.lower() in f.lower()]
        print(f"MODEL_FILTER '{MODEL_FILTER}': Processing {len(jsonl_files)} files")

    if TEMP_FILTER:
        jsonl_files = [f for f in jsonl_files if f"_{TEMP_FILTER}.jsonl" in f]
        print(f"TEMP_FILTER '{TEMP_FILTER}': Processing {len(jsonl_files)} files")

    if LANG_FILTER:
        if LANG_FILTER.lower() == 'java':
            jsonl_files = [f for f in jsonl_files if 'java' in f.lower()]
        elif LANG_FILTER.lower() == 'python':
            jsonl_files = [f for f in jsonl_files if 'java' not in f.lower() and 'cpp' not in f.lower()]
        elif LANG_FILTER.lower() == 'cpp':
            jsonl_files = [f for f in jsonl_files if 'cpp' in f.lower()]
        print(f"LANG_FILTER '{LANG_FILTER}': Selective extraction from {len(jsonl_files)} files")

    if ONLY_GITHUB:
        jsonl_files = [f for f in jsonl_files if f.startswith('github-dataset_')]
        print(f"ONLY_GITHUB filter: Processing {len(jsonl_files)} files")

    print(f"      Processing {len(jsonl_files)} JSONL files...")
    for f_idx, f_name in enumerate(jsonl_files, 1):
        print(f"      [{f_idx}/{len(jsonl_files)}] {f_name}")
        with open(os.path.join(jsonl_folder, f_name), 'r', encoding='utf-8') as f:
            model_name = f_name.replace('.jsonl', '')
            for line_idx, line in enumerate(f):
                if TEST_MODE and line_idx >= 1:
                    break
                try:
                    d = json.loads(line)
                    technique = d.get('technique', 'Assertion')
                    source = d.get('source', 'Author')

                    original_id = d.get('id', 'unknown')
                    if not original_id or original_id == 'unknown':
                        continue

                    ext = os.path.splitext(original_id)[1]
                    item_id_no_ext = os.path.splitext(original_id)[0]

                    item_id = item_id_no_ext
                    prefix = f"{technique}_{source}_"
                    if item_id.startswith(prefix):
                        item_id = item_id[len(prefix):]

                    generations = d.get('generations', {})
                    if generations:
                        for lang_key, code_list in generations.items():
                            for idx, code_obj in enumerate(code_list):
                                if TEST_MODE and (lang_key != 'English' or idx >= 1):
                                    continue

                                code = code_obj.get('cleared_code', '')
                                if not code:
                                    continue

                                if ext == '.java':
                                    code = fix_java_code(code, item_id, technique, source)
                                elif ext == '.py':
                                    # Basic cleaning for Python too, especially for Starcoder
                                    code = strip_starcoder_tokens(code)
                                    code = extract_code_block(code)

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
                        outputs = d.get('output', [])
                        if not isinstance(outputs, list):
                            outputs = [outputs]

                        for idx, out in enumerate(outputs):
                            if TEST_MODE and idx >= 1:
                                break
                            if isinstance(out, dict):
                                code = out.get('cleared_code', '')
                            else:
                                code = out

                            if not code:
                                continue

                            if ext == '.java':
                                code = fix_java_code(code, item_id, technique, source)
                            elif ext == '.py':
                                # Basic cleaning for Python too, especially for Starcoder
                                code = strip_starcoder_tokens(code)
                                code = extract_code_block(code)

                            target_dir = os.path.join(temp_folder, f"{model_name}_R{idx+1}")
                            os.makedirs(target_dir, exist_ok=True)
                            target_file = os.path.join(target_dir, f"{technique}__{source}__{item_id}{ext}")
                            with open(target_file, 'w', encoding='utf-8') as tf:
                                tf.write(code)
                except Exception as e:
                    if DEBUG:
                        print(f"Error processing line in {f_name}: {e}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run SALLM tests via Apptainer/Singularity.")
    parser.add_argument("--model",  default=None, help="Override MODEL_FILTER (e.g. 'gpt', 'gemini')")
    parser.add_argument("--lang",   default=None, help="Override LANG_FILTER ('Python' or 'Java')")
    parser.add_argument("--github", action="store_true", default=None, help="Set ONLY_GITHUB=True")
    parser.add_argument("--no-github", dest="github", action="store_false", help="Set ONLY_GITHUB=False")
    parser.add_argument("--test-mode", action="store_true", default=None, help="Enable TEST_MODE")
    cli = parser.parse_args()

    # CLI overrides — after parsing, update module-level vars so forked workers see correct values
    if cli.model is not None:
        MODEL_FILTER = cli.model
    if cli.lang is not None:
        LANG_FILTER = cli.lang
    if cli.github is not None:
        ONLY_GITHUB = cli.github
    if cli.test_mode:
        TEST_MODE = True
    # Recompute paths after any CLI overrides
    TEMP_PATH, TEST_MODEL_RESULTS = _compute_paths(MODEL_FILTER, ONLY_GITHUB, LANG_FILTER)

    print("=" * 60)
    print(f"  SALLM Evaluation — run_tests_singularity.py")
    print(f"  Model  : {MODEL_FILTER or '(all)'}")
    print(f"  Lang   : {LANG_FILTER or '(all)'}")
    print(f"  GitHub : {ONLY_GITHUB}")
    print(f"  Workers: {MAX_WORKERS}")
    print(f"  Temp   : {TEMP_PATH}")
    print(f"  Results: {TEST_MODEL_RESULTS}")
    print("=" * 60)

    # Folder management
    if os.path.exists(TEMP_PATH):
        print(f"Removing existing temp folder: {TEMP_PATH}")
        shutil.rmtree(TEMP_PATH)
    os.makedirs(TEMP_PATH, exist_ok=True)
    print(f"Created temp folder: {TEMP_PATH}")

    os.makedirs(TEST_MODEL_RESULTS, exist_ok=True)
    print(f"Created TEST_MODEL_RESULTS folder: {TEST_MODEL_RESULTS}")

    os.makedirs(TEST_RESULTS, exist_ok=True)
    print(f"Created TEST_RESULTS folder: {TEST_RESULTS}")

    os.makedirs(TEST_FOLDER, exist_ok=True)
    print(f"Created test folder: {TEST_FOLDER}")

    os.makedirs(SIF_DIR, exist_ok=True)
    print(f"SIF images directory: {SIF_DIR}")

    # Warm up Maven cache if Java is involved (not needed for C++ or Python)
    if LANG_FILTER is None or LANG_FILTER.lower() == 'java':
        warm_up_maven_cache()

    if RUN_TESTS_ON_GENERATED_CODE:
        print(f"\n[1/4] Extracting code from JSONL files in: {GENERATED_CODE_PATH}")
        t0 = time.time()
        save_generated_code(GENERATED_CODE_PATH, TEMP_PATH)
        print(f"      Extraction done in {time.time()-t0:.1f}s")
        target_dir = TEMP_PATH
    else:
        target_dir = JAVA_DATASET_PATH

    print(f"\n[2/4] Scanning extracted files in: {target_dir}")
    t0 = time.time()
    to_process, unique_prompts = get_all_to_process(target_dir)
    print(f"      Found {len(to_process)} files ({len(unique_prompts)} unique prompts) in {time.time()-t0:.1f}s")

    if MODEL_FILTER:
        print(f"      MODEL_FILTER '{MODEL_FILTER}': Filtering samples...")
        to_process = [p for p in to_process if MODEL_FILTER.lower() in p[0].lower()]
        needed_prompts = set((p[1], p[2], p[3], p[5]) for p in to_process)
        unique_prompts = list(needed_prompts)
        print(f"      → {len(to_process)} samples after model filter")

    if LANG_FILTER:
        print(f"      LANG_FILTER '{LANG_FILTER}': Filtering samples...")
        to_process = [p for p in to_process if LANG_FILTER.lower() in p[4].lower()]
        needed_prompts = set((p[1], p[2], p[3], p[5]) for p in to_process)
        unique_prompts = list(needed_prompts)
        print(f"      → {len(to_process)} samples after lang filter")

    if TEST_MODE:
        print(f"      TEST_MODE is ON: Processing {len(to_process)} samples from all models.")
        needed_prompts = set((p[1], p[2], p[3], p[5]) for p in to_process)
        unique_prompts = list(needed_prompts)

    if not to_process:
        print("No files found to process.")
        sys.exit(0)

    print(f"\n[3/4] Checking SIF images for {len(unique_prompts)} unique prompts...")
    build_base_images(unique_prompts)

    print(f"\n[4/4] Running {len(to_process)} tests with Apptainer ({APPTAINER_BIN}), workers={MAX_WORKERS}...")
    start = time.time()
    workers = 1 if DEBUG else MAX_WORKERS
    with ProcessPoolExecutor(max_workers=workers) as executor:
        list(tqdm(executor.map(process_single_file, to_process), total=len(to_process), desc="Running Tests"))

    elapsed = time.time() - start
    print(f"\nFinished {len(to_process)} tests in {elapsed/60:.2f} minutes ({elapsed/len(to_process):.1f}s each avg).")
