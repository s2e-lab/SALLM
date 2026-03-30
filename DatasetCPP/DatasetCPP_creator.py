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
            
            # Prompt
            prompt = ""
            lines = content.split('\n')
            for line in lines:
                prompt += line + '\n'
                # Stop after the function signature but before the opening brace of implementation if it contains CRLF
                if ' {' in line and '(' in line:
                    break
                # Also stop if we find the implementation markers but keep the docstring
                if 'CWE-' in line or 'Vulnerability:' in line:
                    if not ('*/' in line or '/**' in line):
                        # This is likely inside the implementation
                        # But we want to keep the docstring.
                        # Heuristic: if we are in a comment that isn't the docstring.
                        pass
            
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
