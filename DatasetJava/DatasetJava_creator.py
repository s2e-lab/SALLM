import os
import json
import re

def obfuscate_java_code(content, original_class, new_class="ClassX"):
    # Remove package declaration if present in the final output code
    content = re.sub(r'package\s+[\w\.]+;\s*', '', content)
    
    # Replace all occurrences of original_class with new_class using word boundaries
    content = re.sub(r'\b' + re.escape(original_class) + r'\b', new_class, content)
    
    return content

def main():
    base_dir = "src/main/java/com/sallm"
    test_base_dir = "src/test/java/com/sallm"
    output_file = "dataset_java.jsonl"
    
    java_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".java") and "_cwe" in file:
                java_files.append(os.path.join(root, file))
    
    dataset = []
    print(f"Found {len(java_files)} Java files.")
    
    for file_path in java_files:
        # Extract metadata from path
        parts = file_path.split(os.sep)
        technique = parts[5]
        source = parts[6]
        filename = parts[7]
        sample_id = filename.replace(".java", "")
        
        # Original ID for the dataset
        full_id = f"{technique}_{source}_{sample_id}.java"
        
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Extract package declaration
        package_match = re.search(r'package\s+([\w\.]+);', content)
        package_name = package_match.group(1) if package_match else ""
            
        prompt = ""
        last_doc_end = content.rfind("*/")
        if last_doc_end != -1:
            prompt = content[:last_doc_end + 2]
        else:
            prompt = content.split('{')[0] + "{"
            
        obfuscated_content = obfuscate_java_code(content, sample_id)
        obfuscated_prompt = obfuscate_java_code(prompt, sample_id)
        
        # Load and obfuscate test code
        test_file_name = f"Test{sample_id}.java"
        test_file_path = os.path.join(test_base_dir, technique, source, test_file_name)
        test_code = ""
        if os.path.exists(test_file_path):
            with open(test_file_path, 'r') as tf:
                test_code = tf.read()
            test_code = obfuscate_java_code(test_code, sample_id)
        
        dataset.append({
            'id': full_id,
            'technique': technique,
            'source': source,
            'package': package_name,
            'main_path': file_path,
            'test_path': test_file_path if os.path.exists(test_file_path) else "",
            'original_class': sample_id,
            'obfuscated_class': 'ClassX',
            'prompt': obfuscated_prompt,
            'insecure_code': obfuscated_content,
            'test_code': test_code
        })
        
    with open(output_file, 'w') as f:
        for entry in dataset:
            f.write(json.dumps(entry) + '\n')
            
    print(f"Generated {len(dataset)} entries in {output_file}")

if __name__ == "__main__":
    main()
