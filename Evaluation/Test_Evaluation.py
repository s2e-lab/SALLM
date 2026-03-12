import json
import os
import pandas as pd

# Get list of all files in the directory
files = os.listdir('./../Generation/Filtered_Output/')
jsonl_files = sorted([file for file in files if file.endswith('.jsonl') and 
                      ('dataset_java_nl_prompt_best' in file)])
print(len(jsonl_files))

import csv
def get_result(file_path):
    test_success = None
    test_vulnerability = None

    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            return None, None
            
        if not headers:
            return None, None

        if 'TestName' in headers:
            # Format 1: TestName, Result, Message
            try:
                name_idx = headers.index('TestName')
                result_idx = headers.index('Result')
            except ValueError:
                return None, None
                
            for row in reader:
                if len(row) > max(name_idx, result_idx):
                    tname = row[name_idx].lower()
                    res = str(row[result_idx]).lower()
                    mapped_res = None
                    if res in ('success', 'pass', 'passed', 'true'):
                        mapped_res = 'success'
                    elif res in ('failure', 'fail', 'failed', 'error', 'false'):
                        mapped_res = 'failure'

                    if 'correctness' in tname:
                        test_success = mapped_res
                    if 'vulnerability' in tname:
                        test_vulnerability = mapped_res
                        
        elif 'test' in headers:
            # Format 2: test, status, error_reason
            try:
                test_idx = headers.index('test')
                status_idx = headers.index('status')
            except ValueError:
                return None, None
                
            for row in reader:
                if len(row) > max(test_idx, status_idx):
                    status = str(row[status_idx]).lower()
                    if status in ('success', 'pass', 'passed', 'true'):
                        result = 'success'
                    elif status in ('failure', 'fail', 'failed', 'error', 'false'):
                        result = 'failure'
                    else:
                        result = None
                        
                    tname = str(row[test_idx]).lower()
                    if 'functionality' in tname or 'correctness' in tname:
                        test_success = result
                    if 'security' in tname or 'vulnerability' in tname:
                        test_vulnerability = result

    return test_success, test_vulnerability

GENERATION_DIR = './../Generation/Filtered_Output/'

import multiprocessing

def process_file(file_name):
    print(f"Processing {file_name}...")
    # Determine results directory based on file type
    is_java = 'dataset_java' in file_name
    is_github = file_name.startswith('github-dataset')
    if is_java and is_github:
        TEST_MODELS_RESULTS_DIR = './TestModelsResults_GitHub_Java'
    elif is_java:
        TEST_MODELS_RESULTS_DIR = './TestModelsResults_Java'
    elif is_github:
        TEST_MODELS_RESULTS_DIR = './TestModelsResults_GitHub_Python'
    else:
        TEST_MODELS_RESULTS_DIR = './TestModelsResults_Python'

    # Extract temp
    try:
        temp = file_name.rsplit('_', 1)[1].replace('.jsonl', '')
    except:
        print(f"Skipping {file_name}, cannot parse temp")
        return
        
    model_base_name = file_name.replace('.jsonl', '')

    with open(GENERATION_DIR + file_name, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f.readlines()]

    for i in range(len(data)):
        # Robust ID extraction
        original_id = data[i].get('id', 'unknown')
        if not original_id or original_id == 'unknown':
            continue
        
        ext = os.path.splitext(original_id)[1]
        item_id_no_ext = os.path.splitext(original_id)[0]
        
        technique = data[i].get('technique', 'Assertion')
        source = data[i].get('source', 'Author')
        
        # Clean item_id
        item_id = item_id_no_ext
        prefix = f"{technique}_{source}_"
        if item_id.startswith(prefix):
            item_id = item_id[len(prefix):]
            
        # Determine Language
        is_java_dataset = 'dataset_java' in file_name
        language = "Java" if is_java_dataset else "Python"
        
        generations = data[i].get('generations', {})
        
        if generations:
             for lang_key, code_list in generations.items():
                for idx, code_obj in enumerate(code_list):
                    if '_' in model_base_name:
                        parts = model_base_name.rsplit('_', 1)
                        dir_name = f"{parts[0]}_{lang_key}_{parts[1]}"
                    else:
                        dir_name = f"{model_base_name}_{lang_key}"
                        
                    parent_dir_name = f"{dir_name}_R{idx+1}"
                    result_filename = f"Model_{parent_dir_name}_{language}_{technique}_{item_id}_results.csv"
                    result_file = os.path.join(TEST_MODELS_RESULTS_DIR, f"temp_{temp}", result_filename)
                    
                    test_success = None
                    test_vulnerability = None
                    if os.path.exists(result_file):
                        test_success, test_vulnerability = get_result(result_file)
                        
                    # Update the object in memory
                    if isinstance(code_obj, dict):
                        code_obj['test_success'] = test_success
                        code_obj['test_vulnerability'] = test_vulnerability
                    elif isinstance(code_list, list) and isinstance(code_list[idx], dict):
                        code_list[idx]['test_success'] = test_success
                        code_list[idx]['test_vulnerability'] = test_vulnerability
        else:
            # Fallback for 'output' field
            outputs = data[i].get('output', [])
            if not isinstance(outputs, list):
                outputs = [outputs]
                
            for j in range(len(outputs)):
                parent_dir_name = f"{model_base_name}_R{j+1}"
                result_filename = f"Model_{parent_dir_name}_{language}_{technique}_{item_id}_results.csv"
                result_file = os.path.join(TEST_MODELS_RESULTS_DIR, f"temp_{temp}", result_filename)
                
                test_success = None
                test_vulnerability = None
                if os.path.exists(result_file):
                    test_success, test_vulnerability = get_result(result_file)
                
                # Handle if output is list of dicts or strings
                if isinstance(data[i].get('output', [])[j], dict):
                    data[i]['output'][j]['test_success'] = test_success
                    data[i]['output'][j]['test_vulnerability'] = test_vulnerability

    os.makedirs('./TestResults/', exist_ok=True)
    with open('./TestResults/' + file_name, 'w', encoding='utf-8') as f:
        for item in data:
            f.write("%s\n" % json.dumps(item, ensure_ascii=False))
    print(f"Finished {file_name}")

if __name__ == '__main__':
    with multiprocessing.Pool(12) as pool:
        pool.map(process_file, jsonl_files)
    print("All files processed!")




