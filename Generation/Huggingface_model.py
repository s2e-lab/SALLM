# %%
import os
import sys
import json
import re
from tqdm import tqdm
import torch
import logging
import warnings
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from transformers import logging as hf_logging

# Suppress warnings
warnings.filterwarnings("ignore")
hf_logging.set_verbosity_error()

# %%
# Model choice
model_name = "bigcode/starcoder2-3b"
# model_name = "Qwen/Qwen2.5-Coder-3B-Instruct"
# Initialize model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, padding_side='left')
# Fix for missing pad_token (Starcoder/GPT2 models often lack it)
if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

# Trying 'dtype' instead of 'torch_dtype' if that's what the warning implies, 
# though torch_dtype IS the standard arg. 
# However, to be safe against the specific warning observed:
model = AutoModelForCausalLM.from_pretrained(
    model_name, trust_remote_code=True, device_map="auto", torch_dtype=torch.bfloat16
)

# Pipeline setup
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
)

# %%
def extract_docstring_range(code):
    docstring_pattern = r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|/\*\*[\s\S]*?\*/'
    match = re.search(docstring_pattern, code)
    if match:
        start, end = match.span()
        original = match.group(0)
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
    
    if original.startswith('"""'):
        replacement = f'"""\n{new_docstring}\n{indent}"""'
    elif original.startswith("'''"):
        replacement = f"'''\n{new_docstring}\n{indent}'''"
    elif original.startswith("/**"):
        lines = new_docstring.split('\n')
        formatted_lines = [f"{indent} * {line}" for line in lines]
        replacement = "/**\n" + "\n".join(formatted_lines) + f"\n{indent} */"
    else:
        replacement = new_docstring

    return code[:start] + replacement + code[end:]

def create_prompt(prompt_text, language):
    system_message = (
        f"You are an expert programmer and understand {language}. Only output the code without any explanation."
    )
    return f"<|system|>\n{system_message}\n<|user|>\n{prompt_text}\n<|assistant|>\n"

# %%
def prepare_batch_prompts(data):
    prompts = []
    metadata = []
    
    for idx, item in enumerate(data):
        file_ext = os.path.splitext(item.get('main_path', ''))[-1].lower()
        if '.py' in file_ext:
            lang = "Python"
        elif '.java' in file_ext:
            lang = "Java"
        else:
            lang = "Programming Language"
            
        original_prompt = item.get('prompt', '')

        # 1. English
        full_prompt_en = create_prompt(original_prompt, lang)
        prompts.append(full_prompt_en)
        metadata.append({'index': idx, 'lang': 'English', 'prompt_len': len(full_prompt_en)})

        # 2. Translations
        if 'translations' in item:
            for target_lang, trans_data in item['translations'].items():
                if isinstance(trans_data, dict) and 'translation' in trans_data:
                    trans_doc = trans_data['translation']
                    modified_prompt = replace_docstring(original_prompt, trans_doc)
                    full_prompt_trans = create_prompt(modified_prompt, lang)
                    prompts.append(full_prompt_trans)
                    metadata.append({'index': idx, 'lang': target_lang, 'prompt_len': len(full_prompt_trans)})
                    
    return prompts, metadata

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

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "Output")
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    print(f"[{datetime.now()}] Preparing prompts...", flush=True)
    all_prompts, all_metadata = prepare_batch_prompts(data)
    print(f"Total generations per temperature: {len(all_prompts)}", flush=True)

    # temperatures = [ 0.6, 0.8, 1.0]
    # temperatures = [ 0.0, 0.2, 0.4]
    temperatures = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

    for temp in temperatures:
        print(f"[{datetime.now()}] Processing Temperature: {temp}", flush=True)
        
        if temp == 0.0:
            # Greedy decoding
            # Explicitly set temperature to None or don't pass it.
            # Warning about 'generation flags ignored: temperature' usually occurs because
            # defaults in generation_config are present.
            # We can try to silence it or ignore it.
            # Setting do_sample=False is correct.
            gen_kwargs = {
                "max_new_tokens": 2048,
                "do_sample": False,
                "num_return_sequences": 1,
                "pad_token_id": tokenizer.eos_token_id,
                # "temperature": 1.0 # Sometimes explicit dummy value helps silence? No.
            }
        else:
            gen_kwargs = {
                "max_new_tokens": 2048,
                "do_sample": True,
                "temperature": temp,
                "top_p": 1.0,
                "num_return_sequences": 10,
                "pad_token_id": tokenizer.eos_token_id
            }

        results_map = { i: {} for i in range(len(data)) } 
        
        # Batch size
        batch_size = 8 
        
        output_iterator = generator(all_prompts, batch_size=batch_size, **gen_kwargs)
        
        for i, out in enumerate(tqdm(output_iterator, total=len(all_prompts))):
            meta = all_metadata[i]
            idx = meta['index']
            lang = meta['lang']
            
            generated_texts = []
            for o in out:
                full_text = o['generated_text']
                if full_text.startswith(all_prompts[i]):
                     generated_texts.append(full_text[len(all_prompts[i]):].strip())
                else:
                     generated_texts.append(full_text.strip())
            
            results_map[idx][lang] = generated_texts

        processed_records = []
        for i, item in enumerate(data):
            result_item = item.copy()
            result_item['generations'] = results_map[i]
            processed_records.append(result_item)

        output_file = os.path.join(output_dir, f"{base_name}_starcoder2_{temp}.jsonl")
        print(f"Saving to {output_file}")
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for record in processed_records:
                out_f.write(json.dumps(record, ensure_ascii=False) + '\n')

# %%
def main():
    if len(sys.argv) < 2:
        print("Usage: python Huggingface_model.py <input_file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        sys.exit(1)

    process_file(input_path)

if __name__ == "__main__":
    main()
