import json
import os
import sys
import re
import time
import requests
from tqdm import tqdm
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# %%
script_dir = os.path.dirname(os.path.abspath(__file__))
# Note: Ollama doesn't typically need a key, but we'll keep the config loading pattern
# if other integrations need it. 
# config_path = os.path.join(script_dir, "config.json")

model_name = "starcoder2:3b"
OLLAMA_URL = "http://localhost:11434/api/generate"
MAX_WORKERS = 12  # Increased for better utilization of requested cores

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
def ollama_response(prompt_text, language, temperature, max_tokens, num_predict=1):
    """
    Calls Ollama API to generate code.
    Note: Ollama's /api/generate doesn't natively support 'n' (multiple completions) 
    in a single request as efficiently as OpenAI. We'll handle multiple completions
    by calling it multiple times if needed, or stick to n=1 for speed as requested.
    User asked to make it faster.
    """
    try:
        system_message = f"You are an expert programmer and understand {language}. Only output the code without any explanation."
        full_prompt = f"<|system|>\n{system_message}\n<|user|>\n{prompt_text}\n<|assistant|>\n"
        
        payload = {
            "model": model_name,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
                "top_p": 1.0,
                "stop": ["<|endoftext|>", "<|file_separator|>", "<|user|>", "<|system|>", "<|assistant|>"]
            }
        }
        
        outputs = []
        # The user's other scripts (gpt, qwen) use n=10.
        # To make it "faster", we could reduce n, but to be consistent with evaluation, 
        # we might need 10. Let's do 10 calls if temperature > 0, else 1.
        num_generations = 10 if temperature > 0 else 1
        
        for _ in range(num_generations):
            response = requests.post(OLLAMA_URL, json=payload, timeout=300)
            response.raise_for_status()
            res_json = response.json()
            outputs.append(res_json.get("response", "").strip())
            
        return outputs
    except Exception as e:
        print(f"Error generating for {language}: {e}")
        return ['Problem occurred.'] * (10 if temperature > 0 else 1)

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
    generations['English'] = ollama_response(original_prompt, lang, temp, 2048)
    
    # 2. Other Languages
    if 'translations' in item:
        for target_lang, trans_data in item['translations'].items():
            if isinstance(trans_data, dict) and 'translation' in trans_data:
                trans_doc = trans_data['translation']
                modified_prompt = replace_docstring(original_prompt, trans_doc)
                generations[target_lang] = ollama_response(modified_prompt, lang, temp, 2048)
    
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

    # Simplified temperature list to speed up as per user request, 
    # but keeping the common ones if they want full evaluation.
    # User said "make it faster", so maybe just one or two temps? 
    # Let's keep the standard ones but skip 0.0 if not strictly needed, 
    # or just do the full set if they are used to it.
    temperatures = [1.0, 0.8, 0.6, 0.4, 0.2]
    
    
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
        safe_model_name = model_name.replace(":", "_")
        output_file = os.path.join(output_dir, f"{base_name}_{safe_model_name}_{temp}.jsonl")
        print(f"Saving to {output_file}")
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for record in processed_records:
                out_f.write(json.dumps(record, ensure_ascii=False) + '\n')

# %%
def main():
    if len(sys.argv) < 2:
        print("Usage: python Ollama_model.py <input_file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        sys.exit(1)

    process_file(input_path)

if __name__ == "__main__":
    main()
