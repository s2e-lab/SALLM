"""
Equivalent of Test_Evaluation.ipynb.
Reads test result CSVs from TestModelsResults dirs and annotates the
Filtered_Output JSONL files with test_success / test_vulnerability,
saving annotated files to TestResults/.
"""
import json
import os

import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed

GENERATION_DIR = './../Generation/Filtered_Output/'

os.makedirs('./TestResults', exist_ok=True)

# All dataset files (Python std, Python GitHub, Java std, Java GitHub, C++ std, C++ GitHub)
files = os.listdir(GENERATION_DIR)
jsonl_files = sorted([
    f for f in files
    if f.endswith('.jsonl') and (
        f.startswith('dataset_nl_prompt_best') or
        f.startswith('dataset_java_nl_prompt_best') or
        f.startswith('dataset_cpp_nl_prompt_best') or
        (f.startswith('github-dataset_nl_prompt_best') and 'java' not in f and 'cpp' not in f) or
        f.startswith('github-dataset_java_nl_prompt_best') or
        f.startswith('github-dataset_cpp_nl_prompt_best')
    )
])
print(f"Found {len(jsonl_files)} JSONL files")


def get_result(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"  Warning: could not read {file_path}: {e}")
        return None, None

    test_success = None
    test_vulnerability = None

    if 'TestName' in df.columns:
        for _, row in df.iterrows():
            if 'correctness' in str(row['TestName']):
                test_success = row['Result']
            if 'vulnerability' in str(row['TestName']):
                test_vulnerability = row['Result']
    elif 'test' in df.columns:
        for _, row in df.iterrows():
            status = str(row['status']).lower()
            if status in ('pass', 'passed'):
                result = 'success'
            elif status in ('fail', 'failure', 'failed'):
                result = 'failure'
            else:
                result = None
            test_name = str(row['test']).lower()
            if 'functionality' in test_name or 'correctness' in test_name:
                test_success = result
            if 'security' in test_name or 'vulnerability' in test_name:
                test_vulnerability = result

    return test_success, test_vulnerability


def process_one_jsonl(args):
    """
    Worker function to process a single JSONL file and annotate it with test results.
    """
    file_name, jsonl_files, generation_dir, test_results_base_dir = args
    is_java   = 'dataset_java' in file_name
    is_cpp    = 'dataset_cpp'  in file_name
    is_github = file_name.startswith('github-dataset')

    if is_java and is_github:
        test_models_results_dir = './TestModelsResults_GitHub_Java'
    elif is_java:
        test_models_results_dir = './TestModelsResults_Java'
    elif is_cpp and is_github:
        test_models_results_dir = './TestModelsResults_GitHub_Cpp'
    elif is_cpp:
        test_models_results_dir = './TestModelsResults_Cpp'
    elif is_github:
        test_models_results_dir = './TestModelsResults_GitHub_Python'
    else:
        test_models_results_dir = './TestModelsResults_Python'

    try:
        temp = file_name.rsplit('_', 1)[1].replace('.jsonl', '')
    except Exception:
        return f"Skipping {file_name}, cannot parse temp"

    model_base_name = file_name.replace('.jsonl', '')
    print(f"Processing {file_name}...")

    with open(os.path.join(generation_dir, file_name), 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]

    for item in data:
        original_id = item.get('id', 'unknown')
        if not original_id or original_id == 'unknown':
            continue

        item_id_no_ext = os.path.splitext(original_id)[0]
        technique = item.get('technique', 'Assertion')
        source = item.get('source', 'Author')

        item_id = item_id_no_ext
        prefix = f"{technique}_{source}_"
        if item_id.startswith(prefix):
            item_id = item_id[len(prefix):]

        language = "Java" if is_java else ("C++" if is_cpp else "Python")
        generations = item.get('generations', {})

        if generations:
            for lang_key, code_list in generations.items():
                for idx, code_obj in enumerate(code_list):
                    parts = model_base_name.rsplit('_', 1)
                    dir_name = f"{parts[0]}_{lang_key}_{parts[1]}"
                    parent_dir_name = f"{dir_name}_R{idx + 1}"
                    result_filename = (
                        f"Model_{parent_dir_name}_{language}_{technique}_{item_id}_results.csv"
                    )
                    result_file = os.path.join(
                        test_models_results_dir, f"temp_{temp}", result_filename
                    )

                    ts, tv = None, None
                    if os.path.exists(result_file):
                        ts, tv = get_result(result_file)
                    code_obj['test_success'] = ts
                    code_obj['test_vulnerability'] = tv
        else:
            outputs = item.get('output', [])
            if not isinstance(outputs, list):
                outputs = [outputs]

            for j, choice in enumerate(outputs):
                parent_dir_name = f"{model_base_name}_R{j + 1}"
                result_filename = (
                    f"Model_{parent_dir_name}_{language}_{technique}_{item_id}_results.csv"
                )
                result_file = os.path.join(
                    test_models_results_dir, f"temp_{temp}", result_filename
                )

                ts, tv = None, None
                if os.path.exists(result_file):
                    ts, tv = get_result(result_file)

                if isinstance(item['output'][j], dict):
                    item['output'][j]['test_success'] = ts
                    item['output'][j]['test_vulnerability'] = tv

    out_path = os.path.join(test_results_base_dir, file_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    return f"Done {file_name}"


def main():
    # All dataset files (Python std, Python GitHub, Java std, Java GitHub, C++ std, C++ GitHub)
    files = os.listdir(GENERATION_DIR)
    jsonl_files = sorted([
        f for f in files
        if f.endswith('.jsonl') and (
            f.startswith('dataset_nl_prompt_best') or
            f.startswith('dataset_java_nl_prompt_best') or
            f.startswith('dataset_cpp_nl_prompt_best') or
            (f.startswith('github-dataset_nl_prompt_best') and 'java' not in f and 'cpp' not in f) or
            f.startswith('github-dataset_java_nl_prompt_best') or
            f.startswith('github-dataset_cpp_nl_prompt_best')
        )
    ])
    print(f"Found {len(jsonl_files)} JSONL files. Processing in parallel...")
    
    test_results_base_dir = './TestResults'
    os.makedirs(test_results_base_dir, exist_ok=True)

    # Use ProcessPoolExecutor to speed up (FS lookups are slow)
    with ProcessPoolExecutor(max_workers=32) as executor:
        args_list = [(f, jsonl_files, GENERATION_DIR, test_results_base_dir) for f in jsonl_files]
        futures = {executor.submit(process_one_jsonl, args): args[0] for args in args_list}
        
        for future in as_completed(futures):
            res = future.result()
            if res.startswith("Skipping"):
                print(res)

    print("Done — all files written to TestResults/")


if __name__ == "__main__":
    main()
