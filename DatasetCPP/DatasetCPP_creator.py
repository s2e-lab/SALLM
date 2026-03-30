import os
import json

def generate_jsonl(src_dir, test_dir, output_file, is_github=False):
    dataset = []
    
    # Categories for DatasetCPP
    categories = ['Assertion', 'Matching', 'Tainted']
    if is_github:
        categories = ['GitHub']

    for category in categories:
        category_src = os.path.join(src_dir, category)
        if not os.path.exists(category_src):
            continue
            
        for filename in sorted(os.listdir(category_src)):
            if not filename.endswith('.cpp'):
                continue
                
            file_path = os.path.join(category_src, filename)
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Technique and Source
            technique = category
            if is_github:
                source = "GitHub"
            else:
                # Filename format: Source_CWE_Index.cpp (e.g. A_cwe020_0.cpp)
                parts = filename.split('_')
                source_code = parts[0]
                source_map = {
                    'A': 'Author',
                    'codeql': 'CodeQL',
                    'SE': 'SecurityEval',
                    'SO': 'StackOverflow',
                    'SS': 'SonarSource',
                    'Mitre': 'Mitre'
                }
                source = source_map.get(source_code, source_code)

            # Insecure Code (Full content)
            insecure_code = content
            
            # Prompt extraction logic: find target class -> find its first docstringed method
            base_class_name = os.path.splitext(filename)[0]
            lines = content.split('\n')
            
            # Find class start
            class_idx = -1
            for i, line in enumerate(lines):
                if f"class {base_class_name}" in line:
                    class_idx = i
                    break
            
            prompt = ""
            if class_idx != -1:
                # Find first docstring inside target class
                doc_start_idx = -1
                for i in range(class_idx, len(lines)):
                    if "/*" in lines[i] or "/**" in lines[i]:
                        doc_start_idx = i
                        break
                
                if doc_start_idx != -1:
                    # Find first function signature after docstring
                    for i in range(doc_start_idx, len(lines)):
                        if "*/" in lines[i]:
                            for j in range(i, len(lines)):
                                if ' {' in lines[j] and '(' in lines[j]:
                                    prompt = '\n'.join(lines[:j+1]) + '\n'
                                    break
                            if prompt: break
            
            # Fallback if specific heuristic fails
            if not prompt:
                for i, line in enumerate(lines):
                    if f"class {base_class_name}" in line:
                        for j in range(i, len(lines)):
                            if ' {' in lines[j] and '(' in lines[j]:
                                prompt = '\n'.join(lines[:j+1]) + '\n'
                                break
                        if prompt: break
            if not prompt:
                prompt = '\n'.join(lines[:len(lines)//2]) + '\n'
            
            # Test Code
            test_filename = f"test_{filename}"
            test_file_path = os.path.join(test_dir, category, test_filename)
            test_code = ""
            if os.path.exists(test_file_path):
                with open(test_file_path, 'r') as f:
                    test_code = f.read()

            entry = {
                "id": filename,
                "technique": technique,
                "source": source,
                "prompt": prompt.strip() + "\n",
                "insecure_code": insecure_code,
                "test_code": test_code
            }
            dataset.append(entry)

    with open(output_file, 'w') as f:
        for entry in dataset:
            f.write(json.dumps(entry) + '\n')
    
    print(f"Generated {len(dataset)} entries in {output_file}")

if __name__ == "__main__":
    # Generate DatasetCPP.jsonl (100 samples)
    generate_jsonl('src', 'test', 'DatasetCPP.jsonl', is_github=False)
