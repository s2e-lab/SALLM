import re
import sys
import os
import json

def extract_docstrings(prompt):
    # Support Python triple quotes, Javadoc (/**), and standard C (/*) comments
    # Using more robust regex for C-style comments to handle all whitespace/indentation
    docstring_pattern = r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|/\*\*?[\s\S]*?\*/'
    matches = re.findall(docstring_pattern, prompt)
    cleaned_matches = []
    for match in matches:
        if match.startswith('"""') or match.startswith("'''"):
            cleaned = match.strip('"""').strip("'''").strip()
        elif match.startswith('/*'):
            # Java/C docstring: remove /* or /**, */ and the leading asterisks on each line
            start_offset = 3 if match.startswith('/**') else 2
            inner = match[start_offset:-2].strip()
            
            # Remove leading spaces and optional '*' from each line
            lines = []
            for line in inner.splitlines():
                line = line.strip()
                if line.startswith('*'):
                    line = line[1:].strip()
                if line:
                    lines.append(line)
            cleaned = '\n'.join(lines).strip()
            
            # Simple heuristic: ignore very short comments or those that look like markers
            if len(cleaned) < 5:
                continue
                
        if cleaned:
            cleaned_matches.append(cleaned)
    return ' | '.join(cleaned_matches) if cleaned_matches else ''

def read_json_file(file_path):
    print("Reading JSON file...")
    with open(file_path, 'r') as infile:
        data = json.load(infile)
    print("JSON file read successfully.")
    return data

def read_jsonl_file(file_path):
    print("Reading JSONL file...")

    with open(file_path, 'r') as infile:
        lines = infile.readlines()

    json_data = [json.loads(line) for line in lines]
    print("JSONL file read successfully.")
    
    return json_data

def process_docstrings(json_data, key):
    print("Processing docstrings...")

    new_columnName = key + '_nl_prompt'
    updated_data = []
    
    for data in json_data:
        print('key: ', key)
        if key in data:
            print('key value: ', data[key])
            key_value = data[key]
            docstring = extract_docstrings(key_value)
        else:
            docstring = ""
        
        print('docstring: ', docstring)
        data[new_columnName] = docstring
        updated_data.append(data)
    
    print("Processed docstrings")
    return updated_data
        
def save_processed_data(json_data, new_filePath):
    if os.path.exists(new_filePath):
        print(new_filePath+" already exists. No need to proceed.")
        return

    print("Saving processed data to "+new_filePath)
    with open(new_filePath, 'w') as outfile:
        for data in json_data:
            outfile.write(json.dumps(data) + '\n')
    
    print("Processing completed. Data saved to "+new_filePath)


def process_file(file_path, key):
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    extension = os.path.splitext(file_path)[-1].lower()

    print("Base name: " + base_filename + " Extension: " + extension)

    new_directory = "ProcessedFiles"
    os.makedirs(new_directory, exist_ok=True)
    new_filePath = os.path.join(new_directory, base_filename + '_nl_prompt' + extension)
    print("New file name: " + new_filePath)

    if extension != '.jsonl' and extension != '.json':
        print("Unsupported file extension")
    
    if extension == '.jsonl':
        json_data = read_jsonl_file(file_path)
    else:
        json_data = read_json_file(file_path)
    processed_data = process_docstrings(json_data, key)  
    save_processed_data(processed_data, new_filePath)  

def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_docstring.py <file_path> <key>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2] 

    if not os.path.exists(file_path):
        print("Error: File {file_path} does not exist.")
        sys.exit(1)

    print("file path                : "+file_path+", key: "+key)

    print("Starting file processing")
    process_file(file_path, key)

if __name__ == "__main__":
    main()
