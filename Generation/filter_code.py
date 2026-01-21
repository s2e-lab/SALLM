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
    Handles unclosed blocks (truncated output).
    """
    # Pattern to find complete markdown code blocks
    pattern = r"```(?:\w+)?\s*\n(.*?)\s*```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        code = match.group(1)
    else:
        # Check for unclosed block
        start_pattern = r"```(?:\w+)?\s*\n"
        start_match = re.search(start_pattern, text)
        if start_match:
            code = text[start_match.end():]
            # Remove trailing backticks if any (redundant but safe)
            code = code.split('```')[0]
        else:
            # If no block found, assume the whole text is code (or already stripped)
            code = text
            
    if dedent:
        # textwrap.dedent only works on common whitespace.
        # We also need to strip any leading/trailing empty lines.
        return textwrap.dedent(code.strip('\n')).strip()
    else:
        return code.strip()

def fix_truncated_java(code):
    """
    Cleans up truncated Java code by removing incomplete lines and closing braces.
    """
    if not code: return code
    stripped = code.rstrip()
    lines = stripped.split('\n')
    if not lines: return code
    
    last_line = lines[-1].strip()
    
    # 1. Remove obvious truncated imports or statements
    # Ends with a letter/digit and doesn't have a terminator
    if re.search(r'[a-zA-Z0-9]$', last_line):
        if not last_line.endswith(';') and not last_line.endswith('{') and not last_line.endswith('}'):
            lines = lines[:-1]
            stripped = '\n'.join(lines).rstrip()

    # 2. Balance braces
    open_braces = stripped.count('{')
    close_braces = stripped.count('}')
    if open_braces > close_braces:
        # Add missing closing braces
        stripped += '\n' + ('    ' * (open_braces - close_braces - 1)) + '}'
        for i in range(open_braces - close_braces - 2, -1, -1):
            stripped += '\n' + ('    ' * i) + '}'
            
    return stripped

def remove_repetition(prompt, data, is_java=False):
    """
    Removes the part of data that is already present at the end of prompt.
    Also handles Java-specific boilerplate repetition.
    """
    prompt_clean = prompt.strip()
    data_clean = data.lstrip()
    
    # 1. Exact match for full prompt repetition
    if data_clean.startswith(prompt_clean):
        data = data_clean[len(prompt_clean):].lstrip()
        data_clean = data.lstrip()
        
    # 2. Check for line-level repetition (common suffix of prompt and prefix of data)
    p_lines = prompt_clean.split('\n')
    d_lines = data_clean.split('\n')
    
    for i in range(min(len(p_lines), len(d_lines)), 0, -1):
        if p_lines[-i:] == d_lines[:i]:
            data = '\n'.join(d_lines[i:]).lstrip()
            data_clean = data.lstrip()
            break
            
    # 3. Java-specific redundant boilerplate removal
    if is_java:
        prompt_lines_set = set(line.strip() for line in p_lines if line.strip())
        
        d_lines = data.split('\n')
        new_data_lines = []
        for line in d_lines:
            ls = line.strip()
            if not ls:
                new_data_lines.append(ls)
                continue
                
            # If it's a repeated import or package
            if (ls.startswith('import ') or ls.startswith('package ')) and ls in prompt_lines_set:
                continue
            
            # If it's a repeated class declaration
            if ls.startswith('public class ') or ls.startswith('class '):
                # Heuristic: if prompt already has a class declaration
                if any(p_line.strip().startswith('public class ') or p_line.strip().startswith('class ') for p_line in p_lines):
                    continue
            
            new_data_lines.append(line)
        data = '\n'.join(new_data_lines)
            
    return data

split_tokens = ['\ndef', '\nif', '\n@app', "\n'''", '\nclass',"if __name__ == '__main__':", 'if __name__ == "__main__":']

def get_last_function_name_from_code(code, is_java=False):
    """
    Extracts the LAST function name or method signature from the given code string.
    """
    # Split the code into lines
    lines = code.split('\n')
    
    # Iterate through each line REVERSED to find the last function/method definition
    for line in reversed(lines):
        line_s = line.strip()
        if not is_java:
            if line_s.startswith('def '):
                # Extract the function name
                function_name = line.split('(')[0].replace('def ', '').strip()
                return "def "+function_name+'('
        else:
            # Java heuristic: look for method signature patterns
            # Matches: public void name(, private static String name<T>(, etc.
            match = re.search(r'(?:public|private|protected|static|\s) +[\w<>\[\]]+ +(\w+) *\(', line)
            if match:
                # Return the signature up to the paren
                return line[:line.find('(')+1].strip()
    
    return None

def clear_generated_code_gemini(data, item, prompt_key = "prompt"):
    """Gemini cleaner."""
    data = data.split('<|endoftext|>')[0]   
    prompt = item[prompt_key]
    
    # Use extract_code_block to handle any markdown fencing
    data = extract_code_block(data, dedent=True)

    # Detect language
    is_java = ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm'))
    
    # Remove repetition of the prompt
    data = remove_repetition(prompt, data, is_java=is_java)

    function_name = get_last_function_name_from_code(prompt, is_java=is_java)
    if function_name and function_name in data:
        # If the model repeated the function signature, merge
        # Be careful with split: only split at the first occurrence in data
        parts = data.split(function_name, 1)
        prompt_code = parts[0]
        data = parts[1]
        for token in split_tokens:
            if token in data:
                data = data.split(token)[0]

        result = prompt_code + function_name + data
    else:
        # Otherwise append
        for token in split_tokens:
            if token in data:
                data = data.split(token)[0]
        
        # If we are appending to a function signature, ensures body is indented
        if function_name and not is_java: # Only for Python
             # Determine target indentation
             prompt_lines = prompt.rstrip().split('\n')
             last_line = prompt_lines[-1]
             current_indent = 0
             match = re.match(r"^(\s*)", last_line)
             if match:
                 current_indent = len(match.group(1))
             
             target_indent = current_indent
             if last_line.strip().endswith(':'):
                 target_indent += 4
                 
             indent_str = ' ' * target_indent
             
             lines = data.split('\n')
             indented_lines = []
             for line in lines:
                 if line.strip():
                     # Only add indentation if it doesn't already have at least target_indent spaces
                     current_line_indent = len(re.match(r"^(\s*)", line).group(1))
                     if current_line_indent < target_indent:
                         indented_lines.append(indent_str + line.lstrip())
                     else:
                         indented_lines.append(line)
                 else:
                     indented_lines.append(line)
             data = '\n'.join(indented_lines)
             
        result = prompt + '\n' + data

    # Fix truncated code
    if result:
        is_python = ('.py' in item.get('id', '').lower() or 'python' in item.get('id', '').lower())
        if is_python:
            stripped = result.rstrip()
            lines = stripped.split('\n')
            if lines:
                last_line = lines[-1]
                # If last line ends with colon or is a stand-alone keyword
                keywords = ['if', 'else', 'elif', 'try', 'except', 'finally', 'with', 'for', 'while']
                needs_pass = False
                if stripped.endswith(':'):
                    needs_pass = True
                else:
                    # Check if last word is a keyword
                    words = last_line.strip().split()
                    if words and words[-1] in keywords:
                        needs_pass = True
                
                if needs_pass:
                    # Get indentation of last line
                    match = re.match(r"^(\s*)", last_line)
                    indent = len(match.group(1)) if match else 0
                    result = stripped + '\n' + (' ' * (indent + 4)) + 'pass'
        elif is_java:
            result = fix_truncated_java(result)
            
    return result

def post_process_code(code, item):
    """
    Replaces ClassX with original_class and adds package name for Java.
    """
    original_class = item.get('original_class')
    obfuscated_class = item.get('obfuscated_class', 'ClassX')
    package_name = item.get('package')
    
    # Replace ClassX with the original class name
    if original_class and obfuscated_class:
        code = re.sub(r'\b' + re.escape(obfuscated_class) + r'\b', original_class, code)
    
    # Add package declaration for Java if missing
    is_java = '.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm')
    if is_java and package_name:
        if 'package ' not in code[:200]: # check start of file
            code = f"package {package_name};\n\n" + code
            
    return code

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
    
    # Detect language
    is_java = ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm'))
    
    # Remove repetition of the prompt
    new_data = remove_repetition(prompt, new_data, is_java=is_java)
    
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
            
    result = prompt + '\n' + new_data
    
    # Fix truncated code
    if result:
        if is_java:
            result = fix_truncated_java(result)
        else:
            # Python-specific pass injection is handled by Gemini logic, 
            # but let's keep it consistent if needed. 
            # Actually, GPT/Qwen/Starcoder usually provide full blocks if they start.
            pass
            
    return result


# Removed duplicate definition


def clear_generated_code_qwen(data, item, prompt_key = "prompt"):
    data = data.split('<|endoftext|>')[0]   
    
    prompt = item[prompt_key]
    code = extract_code_block(data)

    # Detect language
    is_java = ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm'))
    
    # Remove repetition of the prompt
    code = remove_repetition(prompt, code, is_java=is_java)

    function_name = get_last_function_name_from_code(prompt, is_java=is_java)
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

            result = prompt + '\n' + code
        else:

            prompt_code = code.split(function_name)[0]  
            code = code.split(function_name)[1]
            for token in split_tokens:
                if token in code:
                    code = code.split(token)[0]

            result = prompt_code + function_name + code
    
    else:
        for token in split_tokens:
            if token in code:
                code = code.split(token)[0]
        result = prompt + '\n'+ code
        
    # Fix truncated code
    if result and is_java:
        result = fix_truncated_java(result)
        
    return result

def clear_generated_code_starcoder(data, item, prompt_key = "prompt"):    
    prompt = item[prompt_key]
    
    # Detect language
    is_java = ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm'))
    
    data = extract_assistant_code(data)
    if data is None:
        # Avoid Python-specific 'pass' in Java files
        return prompt + ('\n\tpass' if not is_java else '\n}')
    
    code = extract_code_block(data)
    
    # Remove repetition of the prompt
    code = remove_repetition(prompt, code, is_java=is_java)

    function_name = get_last_function_name_from_code(prompt, is_java=is_java)
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

            result = prompt + '\n' + code
        else:

            prompt_code = code.split(function_name)[0]  
            code = code.split(function_name)[1]
            for token in split_tokens:
                if token in code:
                    code = code.split(token)[0]

            result = prompt_code + function_name + code
    
    else:
        for token in split_tokens:
            if token in code:
                code = code.split(token)[0]
        result = prompt + '\n'+ code
        
    # Fix truncated code
    if result and is_java:
        result = fix_truncated_java(result)
        
    return result

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
                        post_cleaned_code = post_process_code(cleaned_code, item)
                        new_codes.append({
                            'code': old_code,
                            'cleared_code': post_cleaned_code,
                            'compilable': check_compilable(post_cleaned_code)
                        })
                    new_generations[lang] = new_codes
                item['generations'] = new_generations
                cleaned_count += 1
            elif isinstance(item.get('output'), list):
                new_output = []
                for old_code in item['output']:
                    cleaned_code = cleaner_func(old_code, item, prompt_key)
                    post_cleaned_code = post_process_code(cleaned_code, item)
                    new_output.append({
                        'code': old_code,
                        'cleared_code': post_cleaned_code,
                        'compilable': check_compilable(post_cleaned_code)
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
