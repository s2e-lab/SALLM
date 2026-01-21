import json
import os
import ast
import re
from tqdm import tqdm
from datetime import datetime
import textwrap

def extract_code_block(text, dedent=True):
    """
    Extracts code from markdown blocks and dedents it.
    """
    # Pattern to find markdown code blocks
    # Looks for ``` followed by optional language identifier, then content, then ```
    pattern = r"```(?:\w+)?\s*\n(.*?)\s*```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        code = match.group(1)
    else:
        # If no block found, assume the whole text is code (or already stripped)
        code = text
        
    if dedent:
        return textwrap.dedent(code).strip()
    else:
        return code.strip()

split_tokens = ['\ndef', '\nif', '\n@app', "\n'''", '\nclass',"if __name__ == '__main__':", 'if __name__ == "__main__":']

def get_last_function_name_from_code(code):
    """
    Extracts the LAST function name from the given code string.
    """
    # Split the code into lines
    lines = code.split('\n')
    
    # Iterate through each line REVERSED to find the last function definition
    for line in reversed(lines):
        if line.strip().startswith('def '):
            # Extract the function name
            function_name = line.split('(')[0].replace('def ', '').strip()
            return "def "+function_name+'('
    
    return None

def clear_generated_code_gemini(data, item, prompt_key = "prompt"):
    data = data.split('<|endoftext|>')[0]   
    
    prompt = item[prompt_key]
    # Use dedent=True (default) so we start with a clean slate for indentation
    data = extract_code_block(data, dedent=True)

    function_name = get_last_function_name_from_code(prompt)
    if function_name and function_name in data:
        prompt_code = data.split(function_name)[0]  
        data = data.split(function_name)[1]
        for token in split_tokens:
            if token in data:
                data = data.split(token)[0]

        return prompt_code + function_name + data
    
    else:
        for token in split_tokens:
            if token in data:
                data = data.split(token)[0]
        
        # If we are appending to a function signature, ensures body is indented
        if function_name:
             # Determine indentation of the function definition in the prompt
             # We want indentation of the LAST non-empty line
             prompt_lines = prompt.rstrip().split('\n')
             last_line = prompt_lines[-1]
             
             # Calculate existing indentation of the last line (assuming it's the def or docstring)
             current_indent = 0
             match = re.match(r"^(\s*)", last_line)
             if match:
                 current_indent = len(match.group(1))
                 
             # We want the body to be indented by current_indent + 4
             # Since we dedented 'data', we can just prepend this amount
             target_indent = current_indent + 4
             indent_str = ' ' * target_indent
             
             lines = data.split('\n')
             indented_lines = []
             for line in lines:
                 if line.strip():
                     indented_lines.append(indent_str + line)
                 else:
                     indented_lines.append(line)
             data = '\n'.join(indented_lines)
             
        return prompt + '\n'+ data

def extract_assistant_code(text):
    start_tag = "<|assistant|>\n"
    system_tag = "<|system|>\n"
    
    start_idx = text.find(start_tag)
    if start_idx == -1:
        return None  # No assistant tag found

    start_idx += len(start_tag)
    end_idx = text.find(system_tag, start_idx)
    
    if end_idx == -1:
        return text[start_idx:].strip()
    return text[start_idx:end_idx].strip()

def check_compilable(data):
    # Check for Java class structure
    if 'public class' in data or 'class ' in data:
        # Simple heuristic for Java: looks like a class definition
        # We can't easily compile it, but we can assume it's "valid structure" if it looks like Java
        # and we are expecting Java (which we can't fully know here without filename, but data inspection helps)
        # Actually, let's try Python parse first. If it fails, check for Java patterns.
        try:
            ast.parse(data)
            return True
        except:
            if 'public class' in data or ('class ' in data and '{' in data and '}' in data):
                return True
            return False
            
    try:
        ast.parse(data)
        return True
    except:
        return False

def clear_generated_code_gpt(data, item, prompt_key = "prompt"):
    data = data.split('<|endoftext|>')[0]   
    prompt = item[prompt_key]
    
    # Use extract with dedent=False to preserve relative indentation
    new_data = extract_code_block(data, dedent=False)
    
    # Enforce indentation if lines don't start with space (heuristic from notebook)
    lines = new_data.split('\n')
    indented_lines = []
    for line in lines:
        if line.strip() and not line.startswith(' '):
            line = '    ' + line
        indented_lines.append(line)
    new_data = '\n'.join(indented_lines)
    
    # Ensure tokens are removed if present in the extracted code
    for token in split_tokens:
        if token in new_data:
            new_data = new_data.split(token)[0]
            
    return prompt + '\n' + new_data


def clear_generated_code_gemini(data, item, prompt_key = "prompt"):
    """Gemini cleaner from original notebook."""
    data = data.split('<|endoftext|>')[0]   
    
    prompt = item[prompt_key]
    
    # Simple markdown fence stripping from notebook
    lines = data.split('\n')
    if "```python" in lines[0]:
        lines = lines[1:]
    if lines and "```" in lines[-1]:
        lines = lines[:-1]
    data = "\n".join(lines)

    function_name = get_last_function_name_from_code(prompt)
    if function_name and function_name in data:
        prompt_code = data.split(function_name)[0]  
        data = data.split(function_name)[1]
        for token in split_tokens:
            if token in data:
                data = data.split(token)[0]

        return prompt_code + function_name + data
    
    else:
        for token in split_tokens:
            if token in data:
                data = data.split(token)[0]
        return prompt + '\n'+ data


def clear_generated_code_qwen(data, item, prompt_key = "prompt"):
    data = data.split('<|endoftext|>')[0]   
    
    prompt = item[prompt_key]
    code = extract_code_block(data)

    function_name = get_last_function_name_from_code(prompt)
    if function_name and function_name in code:
        
        lines = code.split('\n')
        
        if function_name in lines[0]:
            # Find the second ''' or """ in the code
            for i, line in enumerate(lines[2:]):
                if "'''" in line:
                    lines = lines[i+3:]
                    break
            code = "\n".join(lines)
            for token in split_tokens:
                if token in code:
                    code = code.split(token)[0]

            return prompt + '\n' + code
        else:

            prompt_code = code.split(function_name)[0]  
            code = code.split(function_name)[1]
            for token in split_tokens:
                if token in code:
                    code = code.split(token)[0]

            return prompt_code + function_name + code
    
    else:
        for token in split_tokens:
            if token in code:
                code = code.split(token)[0]
        return prompt + '\n'+ code

def clear_generated_code_starcoder(data, item, prompt_key = "prompt"):    
    prompt = item[prompt_key]
    data = extract_assistant_code(data)
    if data is None:
        return prompt+'\n\tpass'
    
    code = extract_code_block(data)

    function_name = get_last_function_name_from_code(prompt)
    if function_name and function_name in code:
        
        lines = code.split('\n')
        if function_name in lines[0]:
            # Find the second ''' or """ in the code
            for i, line in enumerate(lines[2:]):
                if "'''" in line:
                    lines = lines[i+3:]
                    break
            code = "\n".join(lines)
            for token in split_tokens:
                if token in code:
                    code = code.split(token)[0]

            return prompt + '\n' + code
        else:

            prompt_code = code.split(function_name)[0]  
            code = code.split(function_name)[1]
            for token in split_tokens:
                if token in code:
                    code = code.split(token)[0]

            return prompt_code + function_name + code
    
    else:
        for token in split_tokens:
            if token in code:
                code = code.split(token)[0]
        return prompt + '\n'+ code

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'Output')
    output_dir = os.path.join(base_dir, 'Filtered_Output')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    files = os.listdir(input_dir)
    jsonl_files = [f for f in files if f.endswith('.jsonl') and f.startswith('dataset_')]
    
    print(f"Found {len(jsonl_files)} files to process.")
    
    for filename in tqdm(jsonl_files):
        file_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
        
        # Determine model type from filename
        cleaner_func = None
        if 'gemini' in filename:
            cleaner_func = clear_generated_code_gemini
        elif 'gpt' in filename:
            cleaner_func = clear_generated_code_gpt
        elif 'qwen' in filename:
            cleaner_func = clear_generated_code_qwen
        elif 'starcoder' in filename:
            cleaner_func = clear_generated_code_starcoder
        else:
            print(f"Unknown model in filename: {filename}, skipping.")
            continue
            
        cleaned_count = 0
        for i in range(len(data)):
            item = data[i]
            
            prompt_key = 'prompt'
            if 'translated_prompt' in item:
                prompt_key = 'translated_prompt'
            
            if 'generations' in item and isinstance(item['generations'], dict):
                new_generations = {}
                for lang, codes in item['generations'].items():
                    new_codes = []
                    for old_code in codes:
                        cleaned_code = cleaner_func(old_code, item, prompt_key)
                        new_codes.append({
                            'code': old_code,
                            'cleared_code': cleaned_code,
                            'compilable': check_compilable(cleaned_code)
                        })
                    new_generations[lang] = new_codes
                item['generations'] = new_generations
                cleaned_count += 1
            elif isinstance(item.get('output'), list):
                new_output = []
                for old_code in item['output']:
                    cleaned_code = cleaner_func(old_code, item, prompt_key)
                    new_output.append({
                        'code': old_code,
                        'cleared_code': cleaned_code,
                        'compilable': check_compilable(cleaned_code)
                    })
                data[i]['output'] = new_output
                cleaned_count += 1
            else:
                pass

        with open(output_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
                
    print("Processing complete.")

if __name__ == '__main__':
    main()
