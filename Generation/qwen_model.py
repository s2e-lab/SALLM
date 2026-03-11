# %%
import json
import os
import sys
import re
from tqdm import tqdm
from openai import OpenAI
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# %%
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

with open(config_path) as f:
    config_data = json.loads(f.read())

HF_TOKEN = config_data['HF_TOKEN']
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)
model_name = "Qwen/Qwen2.5-Coder-3B-Instruct"
MAX_WORKERS = 4  # Aligned with job script

# %%
def extract_docstring_range(code):
    """
    Finds the range and indentation of the first docstring in the code.
    Supports Python triple quotes and Java/C /** ... */
    """
    docstring_pattern = r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|/\*\*[\s\S]*?\*/'
    match = re.search(docstring_pattern, code)
    if match:
        start, end = match.span()
        original = match.group(0)
        
        # Check indentation before 'start'
        last_newline = code.rfind('\n', 0, start)
        if last_newline == -1:
            indent = "" 
        else:
            indent = code[last_newline+1:start]
            # Only count as indent if it's purely whitespace
            if not indent.strip() == "":
                indent = "" 
        return start, end, original, indent
    return None

def replace_docstring(code, new_docstring):
    match_info = extract_docstring_range(code)
    if not match_info:
        return code

    start, end, original, indent = match_info
    
    # Construct replacement based on type
    if original.startswith('"""'):
        # Python triple double
        replacement = f'"""\n{new_docstring}\n{indent}"""'
    elif original.startswith("'''"):
        # Python triple single
        replacement = f"'''\n{new_docstring}\n{indent}'''"
    elif original.startswith("/**"):
        # Java/C
        lines = new_docstring.split('\n')
        formatted_lines = [f"{indent} * {line}" for line in lines]
        replacement = "/**\n" + "\n".join(formatted_lines) + f"\n{indent} */"
    else:
        replacement = new_docstring

    return code[:start] + replacement + code[end:]

# %%
def hf_response(prompt_text, language, temperature, max_tokens):
    try:
        messages = [
            {
                "role": "system",
                "content": f"You are an expert programmer and understand {language}. Only output the code without any explanation."
            },
            {
                "role": "user",
                "content": prompt_text + '\n'
            }
        ]
        
        # Hugging Face TGI API requires temperature strictly > 0 if using OpenAI client without explicitly turning off sampling.
        api_temp = max(1e-4, temperature) if temperature < 1e-4 else temperature

        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=api_temp,
            max_tokens=max_tokens,
            top_p=1.0,
            n=10, 
        )
        
        outputs = []
        for choice in response.choices:
            content = choice.message.content.strip()
            outputs.append(content)
        return outputs
    except Exception as e:
        print(f"Error generating for {language}: {e}")
        return ['Problem occurred.'] * 10

def process_single_item(item, temp):
    """
    Process a single item: generate English and translations.
    """
    result_item = item.copy() 
    generations = {}
    
    # Identify language
    file_ext = os.path.splitext(item.get('main_path', ''))[-1].lower()
    if '.py' in file_ext:
        lang = "Python"
    elif '.java' in file_ext:
        lang = "Java"
    else:
        lang = "Programming Language" 

    original_prompt = item.get('prompt', '')

    # 1. English (Default)
    generations['English'] = hf_response(original_prompt, lang, temp, 2048)
    
    # 2. Other Languages
    if 'translations' in item:
        for target_lang, trans_data in item['translations'].items():
            if isinstance(trans_data, dict) and 'translation' in trans_data:
                trans_doc = trans_data['translation']
                modified_prompt = replace_docstring(original_prompt, trans_doc)
                generations[target_lang] = hf_response(modified_prompt, lang, temp, 2048)
    
    result_item['generations'] = generations
    return result_item

# %%
def process_file(file_path):
    print(f"[{datetime.now()}] Reading {file_path}...")
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        if file_path.endswith('.jsonl'):
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
        else:
            data = json.load(f)

    temperatures = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(script_dir, "Output")
    os.makedirs(output_dir, exist_ok=True)

    for temp in temperatures:
        print(f"[{datetime.now()}] Processing Temperature: {temp} with {MAX_WORKERS} workers...")
        processed_records = []
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # Submit all items
            futures = [executor.submit(process_single_item, item, temp) for item in data]
            
            # Use tqdm to show progress as futures complete
            for future in tqdm(as_completed(futures), total=len(futures)):
                try:
                    res = future.result()
                    processed_records.append(res)
                except Exception as e:
                    print(f"Error processing item: {e}")

        # Save output for this temperature
        # Ensure model base name is clean
        safe_model_name = model_name.split("/")[-1]
        output_file = os.path.join(output_dir, f"{base_name}_{safe_model_name}_{temp}.jsonl")
        print(f"Saving to {output_file}")
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for record in processed_records:
                out_f.write(json.dumps(record, ensure_ascii=False) + '\n')

# %%
def main():
    if len(sys.argv) < 2:
        print("Usage: python qwen_model.py <input_file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        sys.exit(1)

    process_file(input_path)

if __name__ == "__main__":
    main()
