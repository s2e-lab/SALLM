import os
import json
import re

DATASET_ROOT = "/Users/lsiddiqsunny/Documents/Notre_Dame/Research/SALLM/GitHubDatasetJava"
SRC_DIR = os.path.join(DATASET_ROOT, "src/main/java/com/sallm/GitHub/GitHub")
TEST_DIR = os.path.join(DATASET_ROOT, "src/test/java/com/sallm/GitHub/GitHub")
OUTPUT_FILE = os.path.join(DATASET_ROOT, "github-dataset_java.jsonl")

def obfuscate_java_code(content, original_class, new_class="ClassX"):
    # Remove package declaration if present
    content = re.sub(r'package\s+[\w\.]+;\s*', '', content)
    
    # Replace all occurrences of original_class with new_class using word boundaries
    content = re.sub(r'\b' + re.escape(original_class) + r'\b', new_class, content)
    
    return content

def main():
    entries = []
    
    # List files in SRC_DIR
    files = sorted([f for f in os.listdir(SRC_DIR) if f.endswith(".java")])
    
    for filename in files:
        if not filename.startswith("GitHub_cwe"):
            continue
            
        file_path = os.path.join(SRC_DIR, filename)
        sample_id = filename.replace(".java", "")
        
        # Technique and Source are fixed for this folder: GitHub/GitHub
        technique = "GitHub"
        source = "GitHub"
        
        # ID format: technique_source_sampleID.java
        full_id = f"{technique}_{source}_{sample_id}.java"
        
        with open(file_path, "r") as f:
            code_content = f.read()
            
        # Extract package declaration
        package_match = re.search(r'package\s+([\w\.]+);', code_content)
        package_name = package_match.group(1) if package_match else ""
        
        # Prompt Logic: Content up to the last Javadoc closing "*/"
        # This includes imports, class definition, and the method javadoc.
        prompt = ""
        last_doc_end = code_content.rfind("*/")
        if last_doc_end != -1:
            prompt = code_content[:last_doc_end + 2]
        else:
            # Fallback if no javadoc found (should not happen in our dataset)
            prompt = code_content.split('{')[0] + "{"
            
        # Obfuscate
        obfuscated_content = obfuscate_java_code(code_content, sample_id)
        obfuscated_prompt = obfuscate_java_code(prompt, sample_id)
        
        # Test file
        test_filename = "Test" + filename
        test_path = os.path.join(TEST_DIR, test_filename)
        test_code = ""
        if os.path.exists(test_path):
            with open(test_path, "r") as f:
                test_code = f.read()
            # Obfuscate test code too
            test_code = obfuscate_java_code(test_code, sample_id)
            
        # Construct Entry
        entry = {
            "id": full_id,
            "technique": technique,
            "source": source,
            "package": package_name,
            "main_path": f"src/main/java/com/sallm/GitHub/GitHub/{filename}",
            "test_path": f"src/test/java/com/sallm/GitHub/GitHub/{test_filename}" if test_code else "",
            "original_class": sample_id,
            "obfuscated_class": "ClassX",
            "prompt": obfuscated_prompt,
            "insecure_code": obfuscated_content,
            "test_code": test_code,
            "language": "Java"
        }
        
        entries.append(entry)
        
    with open(OUTPUT_FILE, "w") as f:
        for entry in entries:
            f.write(json.dumps(entry) + "\n")
            
    print(f"Generated {len(entries)} entries in {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
