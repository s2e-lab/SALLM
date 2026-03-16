# %%
import argparse
import json
import os
import subprocess
import shutil
import sys

# Add parent directory to path to import from Generation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Generation'))
from filter_code import check_compilable, check_compilable_java, remove_misplaced_imports, remove_duplicate_class_definitions, strip_starcoder_tokens, fix_truncated_java, extract_code_block

# %%
# Parse mode from command line
parser = argparse.ArgumentParser()
parser.add_argument('--mode', choices=['python', 'java', 'java_sq'], required=True,
                    help='python: all models, standard+github python datasets; '
                         'java: gemini+gpt, standard+github java datasets; '
                         'java_sq: starcoder2+qwen2.5, standard+github java datasets')
args = parser.parse_args()

files = os.listdir('../Generation/Filtered_Output/')

if args.mode == 'python':
    jsonl_files = [f for f in files if 'java' not in f.lower() and f.endswith('.jsonl')]
elif args.mode == 'java':
    # Default Java mode: Gemini and GPT
    jsonl_files = [f for f in files if 'java' in f.lower() and ('gemini' in f.lower() or 'gpt' in f.lower()) and f.endswith('.jsonl')]
elif args.mode == 'java_sq':
    # Starcoder2 and Qwen2.5
    jsonl_files = [f for f in files if 'java' in f.lower() and ('starcoder2' in f.lower() or 'qwen2.5' in f.lower()) and f.endswith('.jsonl')]
else:
    jsonl_files = []

jsonl_files.sort()

print(f"Mode: {args.mode} — Processing {len(jsonl_files)} files:")
for f in jsonl_files:
    print(f"  {f}")


# %%
def check_tests(path):
    """
    Check if the tests are passing for the given path
    :param path: path to the file
    :return: True if tests are passing, False otherwise
    """
    # Run tests
    try:
        subprocess.check_output(['python', path])
    except subprocess.CalledProcessError:
        return False
    return True

# %%
for file in jsonl_files:

    with open('../Generation/Filtered_Output/' + file, 'r') as f:
        data = [json.loads(line) for line in f.readlines()]

    model_name = file.split('.jsonl')[0]
    print(model_name)
    for i in range(len(data)):
        id = data[i]['id']
        technique =  data[i]['technique']
        source = data[i]['source']
        is_java_dataset = 'java' in file
        language = "Java" if is_java_dataset else "Python"
        if language is None:
            continue
        if language.strip() == '':
            continue
        # Standard ids: {technique}_{source}_{item}  → skip first 2 parts
        # GitHub Python ids: {GitHub}_{cwe}_{n}.py  → only 3 parts, skip 1
        id_parts = id.split('_')
        skip = 2 if len(id_parts) > 3 else 1
        file_name = '_'.join(id_parts[skip:])

        
        dataset_root = f'./Dataset/{model_name}'
        # Check if the folder exists, if not create it
        if is_java_dataset:
            # We use a unique package per file to avoid "duplicate class" errors from helper classes
            java_package_path = f"com/sallm/{technique}/{source}/"
            # We'll append a subfolder per file in the loop below
            base_dir_parent = f'./Dataset/{model_name}/{java_package_path}'
        else:
            base_dir = f'./Dataset/{model_name}/{technique}/{source}/'
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)

        # if technique == 'Assertion' and source in ['Author', 'SonarSource']:

        #     if not os.path.exists(f'./PythonDataset/{technique}/{source}/static'):
        #         shutil.copytree(f'../PythonDataset/{technique}/{source}/static', f'./Dataset/{technique}/{source}/static')


        outputs_with_lang = []
        if 'generations' in data[i]:
            for lang in data[i]['generations']:
                for item in data[i]['generations'][lang]:
                    outputs_with_lang.append((item, lang))
        else:
            # Default to English for legacy output field
            for item in data[i].get('output', []):
                outputs_with_lang.append((item, "English"))

        for j, (output_item, nat_lang) in enumerate(outputs_with_lang):
            # Check if code is marked as compilable
            if not output_item.get('compilable', False):
                continue

            import re

            # Get both code fields
            cleared_code = output_item['cleared_code']
            generated_code = output_item.get('code', '')

            # Strategy: Check if there's an empty method in cleared_code
            # If yes, try to fill it with generated_code
            # If no, use cleared_code as-is

            # Check for empty method pattern
            empty_method_pattern = r'(public|private|protected)?\s*\w+\s+\w+\s*\([^)]*\)\s*\{[\s]*\}'
            has_empty_method = re.search(empty_method_pattern, cleared_code) is not None

            # Clean markdown code blocks from generated code if it exists
            clean_gen = ""
            if generated_code:
                clean_gen = strip_starcoder_tokens(generated_code)
                clean_gen = extract_code_block(clean_gen)

            if has_empty_method and clean_gen and len(clean_gen) >= 20 and is_java_dataset:
                # Try to merge generated code into cleared_code template for Java

                # Validate: skip if too short
                if len(clean_gen) < 30:
                    continue

                # Check brace balance
                if clean_gen.count('{') < clean_gen.count('}') - 1:
                    continue

                # Extract method body from generated code
                if re.match(r'^\s*(public|private|protected)', clean_gen):
                    # Full method - extract body
                    first_brace = clean_gen.find('{')
                    if first_brace != -1:
                        brace_count = 0
                        method_end = -1
                        for idx in range(first_brace, len(clean_gen)):
                            if clean_gen[idx] == '{':
                                brace_count += 1
                            elif clean_gen[idx] == '}':
                                brace_count -= 1
                                if brace_count == 0:
                                    method_end = idx
                                    break
                        method_body = clean_gen[first_brace+1:method_end].strip() if method_end != -1 else clean_gen[first_brace+1:].strip()
                    else:
                        method_body = clean_gen
                else:
                    # Already just the body
                    method_body = clean_gen

                # Clean up
                method_body = re.sub(r'\}\s*$', '', method_body).strip()

                # Validate method body
                if not method_body or len(method_body) < 10:
                    continue

                # Find empty method in cleared_code (use same pattern)
                matches = list(re.finditer(empty_method_pattern, cleared_code))

                if matches:
                    last_match = matches[-1]
                    before_body = cleared_code[:last_match.end()-1]
                    after_body = cleared_code[last_match.end():]
                    code = before_body + '\n        ' + method_body + '\n    }'  + after_body
                else:
                    continue
            elif is_java_dataset and clean_gen and len(clean_gen) >= 20 and cleared_code.strip().endswith('}'):
                # Handle case where cleared_code is a class skeleton but has no empty method
                # ONLY inject if clean_gen is not already largely present in cleared_code to avoid duplicates
                # We use a simple containment check (ignoring whitespace)
                if clean_gen.replace(" ", "").replace("\n", "") not in cleared_code.replace(" ", "").replace("\n", ""):
                    last_brace_idx = cleared_code.rfind('}')
                    code = cleared_code[:last_brace_idx] + '\n' + clean_gen + '\n' + cleared_code[last_brace_idx:]
                else:
                    code = cleared_code
            elif cleared_code.count('{') == cleared_code.count('}'):
                # No empty method or no generated code, but cleared_code is balanced - use it
                code = cleared_code
            else:
                # cleared_code is malformed, skip
                continue

            # Clean up Java code using filter_code.py functions
            if is_java_dataset:
                code = remove_duplicate_class_definitions(code)
                code = remove_misplaced_imports(code)

            # Final validation: use comprehensive compilability check from filter_code.py
            if is_java_dataset:
                if not check_compilable_java(code):
                    continue
            else:
                if not check_compilable(code):
                    continue

            # if technique == 'Assertion':
            #     with open(f'./Dataset/{technique}/{source}/{file_name}', 'w') as f:
            #         f.write(code)

            #     with open(f'./Dataset/{technique}/{source}/test_{file_name}', 'w') as f:
            #         f.write(data[i]['test_code'])

            #     data[i]['output'][j]['vulnerable'] = check_tests(f'./Dataset/{technique}/{source}/test_{file_name}')

            #     # print(check_tests(f'./Dataset/{technique}/{source}/test_{file_name}'))

            #     if os.path.exists(f'./Dataset/{technique}/{source}/{file_name}'):
            #         os.remove(f'./Dataset/{technique}/{source}/{file_name}')
            #     if os.path.exists(f'./Dataset/{technique}/{source}/test_{file_name}'):
            #         os.remove(f'./Dataset/{technique}/{source}/test_{file_name}')

            extension = '.java' if is_java_dataset else '.py'
            current_file_extension = '.py' if not is_java_dataset else '.java'
            
            # Remove existing extension from file_name if present to avoid double extensions or wrong ones
            base_file_name = file_name
            if base_file_name.endswith('.py'):
                base_file_name = base_file_name[:-3]
            elif base_file_name.endswith('.java'):
                base_file_name = base_file_name[:-5]
                
            current_file_name = f"{base_file_name}_{j}_{nat_lang}{extension}"
            
            # For Java, the public class name must match the filename and we need a package
            if is_java_dataset:
                import re
                
                def sanitize_code(code_content):
                    # Remove Lombok stuff
                    code_content = re.sub(r'import\s+lombok\..*;', '', code_content)
                    lombok_annotations = [
                        r'@Data', r'@Builder', r'@AllArgsConstructor', r'@NoArgsConstructor', 
                        r'@RequiredArgsConstructor', r'@Getter', r'@Setter', r'@ToString', 
                        r'@EqualsAndHashCode', r'@Value', r'@Slf4j'
                    ]
                    for annotation in lombok_annotations:
                        code_content = re.sub(annotation, '', code_content)
                    
                    # Robust cleaning and reconstruction
                    code_content = strip_starcoder_tokens(code_content)
                    code_content = fix_truncated_java(code_content)
                    code_content = remove_duplicate_class_definitions(code_content)
                    code_content = remove_misplaced_imports(code_content)
                    
                    return code_content

                code = sanitize_code(code)
                class_name_to_use = current_file_name.replace('.java', '')
                
                # Use a unique subfolder/package per prompt AND generation to avoid class conflicts
                # Example: prompt 5, gen 0 -> p_5_f_0
                file_unique_id = f"p_{i}_f_{j}"
                file_base_dir = f"{base_dir_parent}{file_unique_id}"
                if not os.path.exists(file_base_dir):
                    os.makedirs(file_base_dir, exist_ok=True)
                
                # Replace existing package declaration or add a new one
                package_name = f"com.sallm.{technique}.{source}.{file_unique_id}".replace('/', '.')
                package_line = f"package {package_name};"
                if re.search(r'package\s+[\w.]+;', code):
                    code = re.sub(r'package\s+[\w.]+;', package_line, code, count=1)
                else:
                    code = f"{package_line}\n\n" + code
                
                # This regex replaces modifiers + 'class Name' with 'public class NewName'
                # Handles: 'public class', 'class', 'public static class', etc.
                code = re.sub(r'(?:public\s+|private\s+|protected\s+|static\s+|final\s+)*class\s+\w+', f'public class {class_name_to_use}', code, count=1)
                
                save_path = f'{file_base_dir}/{current_file_name}'
            else:
                save_path = f'{base_dir}/{current_file_name}'

            with open(save_path, 'w') as f:
                    f.write(code)


    template_file = 'codeql_job_java_bk.sh' if is_java_dataset else 'codeql_job_bk.sh'
    with open(template_file, 'r') as f:
        codeql_command = f.read()

    codeql_command = codeql_command.replace('MODEL_NAME', model_name)

    with open(f'codeql_job_{model_name}.sh', 'w') as f:
        f.write(codeql_command)

    try:
        subprocess.run(['bash', f'codeql_job_{model_name}.sh'])
        print(f"Completed job for {model_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Error running job for {model_name}:")
        print(e.output.decode())





