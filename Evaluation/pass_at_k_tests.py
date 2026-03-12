import pandas as pd
from typing import List, Union
import itertools

import numpy as np
from collections import defaultdict
import os
import pandas as pd

def estimate_pass_at_k(
    num_samples: Union[int, List[int], np.ndarray],
    num_correct: Union[List[int], np.ndarray],
    k: int
) -> np.ndarray:
    """
    Estimates pass@k of each problem and returns them in an array.
    """

    def estimator(n: int, c: int, k: int) -> float:
        """
        Calculates 1 - comb(n - c, k) / comb(n, k).
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])

final_results = []

import os
# Get list of all files in the directory
files = os.listdir('./TestResults/')
# Include all jsonl files that look like datasets (Python, non-java)
json_files = []
print(len(json_files), "json files found")

import json

final_results = []
for file_name in json_files:
    try:
        # Parse model name and temp from filename
        base_name = file_name.replace('.jsonl', '')
        parts = base_name.split('_')
        temp = parts[-1]
        
        is_github_file = file_name.startswith('github-dataset')
        if 'dataset_java' in file_name:
             model_name_parts = parts[5:-1]
        else:
             model_name_parts = parts[4:-1]
             
        model_name = '_'.join(model_name_parts)
        if is_github_file:
            model_name = 'GitHub_' + model_name
        print(f"Processing {file_name} -> Model: {model_name}, Temp: {temp}")

        with open('./TestResults/' + file_name, 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f]
        
        results = {}
        
        for item in data:
            id = item.get('id', 'unknown')
            
            generations = item.get('generations', {})
            
            if generations:
                for language, code_list in generations.items():
                    if language not in results:
                        results[language] = defaultdict(list)
                    
                    current_id_results = []
                    for code_obj in code_list:
                        # Functional Correctness: 'success' = PASS
                        is_func_correct = code_obj.get('test_success') == 'success'
                        
                        # Vulnerability Check:
                        # Based on test_code inspection: 
                        # AssertLess(duplicates, 100) -> PASS ('success') if VULNERABLE.
                        # Fail ('failure') if SECURE (no duplicates).
                        # We want 'is_secure' to be True if it failed the vulnerability test.
                        is_secure = code_obj.get('test_vulnerability') == 'failure'
                        
                        current_id_results.append([is_func_correct, is_secure])
                    
                    results[language][id] = current_id_results

            elif 'output' in item:
                # Legacy handling
                language = item.get('language', 'Unknown')
                if language == 'Unknown' and 'dataset_java' in file_name: language = 'Java'
                if language == 'Unknown' and 'dataset_nl' in file_name: language = 'Python'
                
                if language not in results:
                    results[language] = defaultdict(list)
                
                outputs = item['output']
                if not isinstance(outputs, list):
                    outputs = [outputs]
                    
                current_id_results = []
                for choice in outputs:
                    if isinstance(choice, dict):
                        is_func_correct = choice.get('test_success') == 'success'
                        is_secure = choice.get('test_vulnerability') == 'failure'
                        current_id_results.append([is_func_correct, is_secure])
                
                if current_id_results:
                    results[language][id] = current_id_results

        # Calculate Metrics per Language
        for language in results.keys():
            current_results = results[language]
            
            # Functionality
            total_func = []
            correct_func = []
            for result in current_results.values():
                total_func.append(len(result))
                correct_func.append(sum(r[0] for r in result))
            
            total_func = np.array(total_func)
            correct_func = np.array(correct_func)
            
            ks = [1, 3, 5]
            pass_at_k = []
            for k in ks:
                if total_func.size > 0 and (total_func >= k).all():
                    pass_at_k.append(estimate_pass_at_k(total_func, correct_func, k).mean() * 100)
                else:
                    pass_at_k.append(0.0)
            print(f"  {language} Pass@k: {pass_at_k}")

            # Security (via Pass@k estimator on 'is_secure')
            total_vul = []
            correct_vul = []
            for result in current_results.values():
                total_vul.append(len(result))
                correct_vul.append(sum(r[1] for r in result)) # Count SECURE ones
            
            total_vul = np.array(total_vul)
            correct_vul = np.array(correct_vul)
            
            # vul_at_k -> actually SECURE@k (Prob at least one is secure)
            vul_at_k = []
            for k in ks:
                if total_vul.size > 0 and (total_vul >= k).all():
                    vul_at_k.append(estimate_pass_at_k(total_vul, correct_vul, k).mean() * 100)
                else:
                    vul_at_k.append(0.0)
            print(f"  {language} Secure@k (Pass@k): {vul_at_k}")

            # Absolute Security (All k are secure)
            security_at_k = []
            for k in ks:
                total_passed = 0
                num_problems = len(current_results.values())
                if num_problems == 0:
                    security_at_k.append(0.0)
                    continue
                    
                for result in current_results.values():
                    if len(result) < k:
                        continue
                    
                    count = 0
                    for i in range(k):
                        if result[i][1]: # is_secure
                            count += 1
                    if count == k:
                        total_passed += 1
                security_at_k.append(total_passed / num_problems * 100)
            print(f"  {language} ConsistentSec@k (All Secure): {security_at_k}")

            final_results.append([
                model_name, temp, language, 
                pass_at_k[0], pass_at_k[1], pass_at_k[2], 
                vul_at_k[0], vul_at_k[1], vul_at_k[2], 
                security_at_k[0], security_at_k[1], security_at_k[2]
            ])
    except Exception as e:
        print(f"Error processing {file_name}: {e}")


df = pd.DataFrame(final_results, columns=['Model', 'Temp', 'Language', 'pass@1', 'pass@3', 'pass@5', 'vul@1', 'vul@3', 'vul@5', 'security@1', 'security@3', 'security@5'])
# Note: vul@k here represents 'Pass@k for Security' (Prob of >=1 secure)
# Note: security@k here represents 'Consistent Security' (Prob of all k secure)
df = df.sort_values(by=['Model', 'Temp', 'Language'])
df.to_csv('./Result/Tests_Results_Python.csv', index=False)
print("Saved to Tests_Results_Python.csv")

import os
# Get list of Java files
files = os.listdir('./TestResults/')
java_json_files = sorted([file for file in files if file.endswith('.jsonl') and 
                          ('dataset_java_nl_prompt_best' in file)])
print(len(java_json_files), "java json files found")

import json

final_results = []
final_results = []
for file_name in java_json_files:
    try:
        # Parse model name and temp from filename
        base_name = file_name.replace('.jsonl', '')
        parts = base_name.split('_')
        temp = parts[-1]
        
        is_github_file = file_name.startswith('github-dataset')
        # Java files always use parts[5:-1]
        model_name_parts = parts[5:-1]
        model_name = '_'.join(model_name_parts)
        if is_github_file:
            model_name = 'GitHub_' + model_name
        print(f"Processing {file_name} -> Model: {model_name}, Temp: {temp}")

        with open('./TestResults/' + file_name, 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f]
        
        results = {}
        
        for item in data:
            id = item.get('id', 'unknown')
            
            generations = item.get('generations', {})
            
            if generations:
                for language, code_list in generations.items():
                    if language not in results:
                        results[language] = defaultdict(list)
                    
                    current_id_results = []
                    for code_obj in code_list:
                        # Functional Correctness: 'success' = PASS
                        is_func_correct = code_obj.get('test_success') == 'success'
                        
                        # Vulnerability Check:
                        # Based on test_code inspection: 
                        # AssertLess(duplicates, 100) -> PASS ('success') if VULNERABLE.
                        # Fail ('failure') if SECURE (no duplicates).
                        # We want 'is_secure' to be True if it failed the vulnerability test.
                        is_secure = code_obj.get('test_vulnerability') == 'failure'
                        
                        current_id_results.append([is_func_correct, is_secure])
                    
                    results[language][id] = current_id_results

            elif 'output' in item:
                # Legacy handling
                language = item.get('language', 'Unknown')
                if language == 'Unknown' and 'dataset_java' in file_name: language = 'Java'
                if language == 'Unknown' and 'dataset_nl' in file_name: language = 'Python'
                
                if language not in results:
                    results[language] = defaultdict(list)
                
                outputs = item['output']
                if not isinstance(outputs, list):
                    outputs = [outputs]
                    
                current_id_results = []
                for choice in outputs:
                    if isinstance(choice, dict):
                        is_func_correct = choice.get('test_success') == 'success'
                        is_secure = choice.get('test_vulnerability') == 'failure'
                        current_id_results.append([is_func_correct, is_secure])
                
                if current_id_results:
                    results[language][id] = current_id_results

        # Calculate Metrics per Language
        for language in results.keys():
            current_results = results[language]
            
            # Functionality
            total_func = []
            correct_func = []
            for result in current_results.values():
                total_func.append(len(result))
                correct_func.append(sum(r[0] for r in result))
            
            total_func = np.array(total_func)
            correct_func = np.array(correct_func)
            
            ks = [1, 3, 5]
            pass_at_k = []
            for k in ks:
                if total_func.size > 0 and (total_func >= k).all():
                    pass_at_k.append(estimate_pass_at_k(total_func, correct_func, k).mean() * 100)
                else:
                    pass_at_k.append(0.0)
            print(f"  {language} Pass@k: {pass_at_k}")

            # Security (via Pass@k estimator on 'is_secure')
            total_vul = []
            correct_vul = []
            for result in current_results.values():
                total_vul.append(len(result))
                correct_vul.append(sum(r[1] for r in result)) # Count SECURE ones
            
            total_vul = np.array(total_vul)
            correct_vul = np.array(correct_vul)
            
            # vul_at_k -> actually SECURE@k (Prob at least one is secure)
            vul_at_k = []
            for k in ks:
                if total_vul.size > 0 and (total_vul >= k).all():
                    vul_at_k.append(estimate_pass_at_k(total_vul, correct_vul, k).mean() * 100)
                else:
                    vul_at_k.append(0.0)
            print(f"  {language} Secure@k (Pass@k): {vul_at_k}")

            # Absolute Security (All k are secure)
            security_at_k = []
            for k in ks:
                total_passed = 0
                num_problems = len(current_results.values())
                if num_problems == 0:
                    security_at_k.append(0.0)
                    continue
                    
                for result in current_results.values():
                    if len(result) < k:
                        continue
                    
                    count = 0
                    for i in range(k):
                        if result[i][1]: # is_secure
                            count += 1
                    if count == k:
                        total_passed += 1
                security_at_k.append(total_passed / num_problems * 100)
            print(f"  {language} ConsistentSec@k (All Secure): {security_at_k}")

            final_results.append([
                model_name, temp, language, 
                pass_at_k[0], pass_at_k[1], pass_at_k[2], 
                vul_at_k[0], vul_at_k[1], vul_at_k[2], 
                security_at_k[0], security_at_k[1], security_at_k[2]
            ])
    except Exception as e:
        print(f"Error processing {file_name}: {e}")


df_java = pd.DataFrame(final_results, columns=['Model', 'Temp', 'Language', 'pass@1', 'pass@3', 'pass@5', 'vul@1', 'vul@3', 'vul@5', 'security@1', 'security@3', 'security@5'])
df_java = df_java.sort_values(by=['Model', 'Temp', 'Language'])
df_java.to_csv('./Result/Tests_Results_Java.csv', index=False)
print("Saved to Tests_Results_Java.csv")



