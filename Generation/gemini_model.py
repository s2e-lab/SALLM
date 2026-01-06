# %%
import json
import os
import sys
import re
import time
from tqdm import tqdm
from google import genai
from google.genai import types
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# %%
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

with open(config_path) as f:
    config_data = json.loads(f.read())

from tenacity import retry, wait_random_exponential, stop_after_attempt, retry_if_exception_type

# ... (imports)

GEMINI_KEY = config_data['GEMINI_KEY']
client = genai.Client(api_key=GEMINI_KEY)
# model_name = "gemini-2.0-flash" 
# User is using 2.5-flash as per error message "model: gemini-2.5-flash"
model_name = "gemini-2.5-flash" 

MAX_WORKERS = 10  # Reduced from 32 to avoid hitting 1000 RPM limit too quickly

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

# ...

# Define a predicate to identify rate limit exceptions
def is_rate_limit_error(exception):
    # Check for typical 429 / Resource Exhausted indicators
    msg = str(exception).lower()
    return "429" in msg or "resource_exhausted" in msg or "quota" in msg

def log_retry(retry_state):
    print(f"[{datetime.now()}] Request failed. Retrying attempt {retry_state.attempt_number}/15. Error: {retry_state.outcome.exception()}")

@retry(
    retry=retry_if_exception_type(Exception),
    wait=wait_random_exponential(multiplier=2, max=60),
    stop=stop_after_attempt(15),
    before_sleep=log_retry
)
def gemini_response_with_retry(prompt_text, language, temperature, max_tokens):
    # This function wraps the API call
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt_text + '\n'],
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
            candidate_count=8,
            presence_penalty=0,
            frequency_penalty=0,
            system_instruction=f"You are an expert programmer and understand {language}. Only output the code without any explanation."
        ),
    )
    
    outputs = []
    if response.candidates:
        for choice in response.candidates:
            if choice.content and choice.content.parts:
                outputs.append(choice.content.parts[0].text.strip())
    return outputs

def gemini_response(prompt_text, language, temperature, max_tokens):
    try:
        return gemini_response_with_retry(prompt_text, language, temperature, max_tokens)
    except Exception as e:
        print(f"Error generating for {language}: {e}")
        return ['Problem occurred.']


def process_single_item(item, temp):
    result_item = item.copy() 
    generations = {}
    
    file_ext = os.path.splitext(item.get('main_path', ''))[-1].lower()
    if '.py' in file_ext:
        lang = "Python"
    elif '.java' in file_ext:
        lang = "Java"
    else:
        lang = "Programming Language" 

    original_prompt = item.get('prompt', '')

    # 1. English
    generations['English'] = gemini_response(original_prompt, lang, temp, 512)
    
    # 2. Translations
    if 'translations' in item:
        for target_lang, trans_data in item['translations'].items():
            if isinstance(trans_data, dict) and 'translation' in trans_data:
                trans_doc = trans_data['translation']
                modified_prompt = replace_docstring(original_prompt, trans_doc)
                generations[target_lang] = gemini_response(modified_prompt, lang, temp, 512)
    
    result_item['generations'] = generations
    return result_item

# %%
import threading

# ... inside process_file ...

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

    file_lock = threading.Lock()

    for temp in temperatures:
        output_file = os.path.join(output_dir, f"{base_name}_{model_name}_{temp}.jsonl")
        
        # 1. Load existing progress
        processed_ids = set()
        if os.path.exists(output_file):
            print(f"[{datetime.now()}] Found existing file {output_file}. checking progress...")
            with open(output_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        try:
                            rec = json.loads(line)
                            # Assuming 'id' or 'main_path' identifies the record. 
                            # If 'id' is unique, use it. data items have 'id'?
                            # Looking at test_input_best.jsonl, it has "id".
                            if 'id' in rec:
                                processed_ids.add(rec['id'])
                            elif 'main_path' in rec:
                                processed_ids.add(rec['main_path'])
                        except:
                            pass
            print(f"[{datetime.now()}] Resuming: {len(processed_ids)} items already processed for temp {temp}.")

        # 2. Filter data
        items_to_process = []
        for item in data:
            item_id = item.get('id') or item.get('main_path')
            if item_id not in processed_ids:
                items_to_process.append(item)
        
        if not items_to_process:
            print(f"[{datetime.now()}] All items processed for temp {temp}. Skipping.")
            continue

        print(f"[{datetime.now()}] Processing Temperature: {temp} with {MAX_WORKERS} workers. Items remaining: {len(items_to_process)}")
        
        # 3. Process remaining (Incremental Write)
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(process_single_item, item, temp) for item in items_to_process]
            
            # Open file in append mode
            with open(output_file, 'a', encoding='utf-8') as out_f:
                for future in tqdm(as_completed(futures), total=len(futures)):
                    try:
                        res = future.result()
                        # Write immediately with lock
                        with file_lock:
                            out_f.write(json.dumps(res, ensure_ascii=False) + '\n')
                            out_f.flush() # Ensure it hits disk
                    except Exception as e:
                        print(f"Error processing item: {e}")

# %%
def main():
    if len(sys.argv) < 2:
        print("Usage: python gemini_model.py <input_file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        sys.exit(1)

    process_file(input_path)

if __name__ == "__main__":
    main()
