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

def remove_duplicate_class_definitions(code):
    """
    Removes duplicate class definitions that may have been inserted mid-code.
    Keeps only the first class definition.
    """
    lines = code.split('\n')

    # Find all lines with class declarations
    class_decl_indices = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^(public\s+)?(abstract\s+)?(final\s+)?class\s+\w+', stripped):
            class_decl_indices.append(i)

    # If we have more than one class declaration, keep only the first one
    if len(class_decl_indices) > 1:
        # Remove everything from the second class declaration onwards
        lines = lines[:class_decl_indices[1]]
        code = '\n'.join(lines)

    return code

def remove_misplaced_imports(code):
    """
    Removes import statements that appear in the middle of a class (not at the top).
    """
    lines = code.split('\n')
    result_lines = []

    # Find where the class starts
    class_started = False
    in_method = False
    brace_count = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track when we've entered the class body
        if re.match(r'^(public\s+)?(abstract\s+)?(final\s+)?class\s+\w+', stripped):
            class_started = True
            result_lines.append(line)
            continue

        # Track brace depth
        brace_count += line.count('{') - line.count('}')

        # If we're inside the class and see an import, skip it
        if class_started and stripped.startswith('import ') and brace_count > 0:
            continue

        # Skip package declarations in the middle of code
        if class_started and stripped.startswith('package ') and brace_count > 0:
            continue

        result_lines.append(line)

    return '\n'.join(result_lines)

def fix_truncated_java(code):
    """
    Cleans up truncated Java code by removing incomplete lines and closing braces.
    Enhanced version that handles multiple issues.
    """
    if not code: return code

    # First, remove duplicate class definitions
    code = remove_duplicate_class_definitions(code)

    # Remove misplaced imports
    code = remove_misplaced_imports(code)

    stripped = code.rstrip()
    lines = stripped.split('\n')
    if not lines: return code

    # Remove obviously conversational junk and HTML from Starcoder/Qwen
    cleaned_lines = []
    for line in lines:
        s = line.strip()
        # Skip HTML tags that are not part of code
        if re.match(r'^<[a-z/].*?>$', s.lower()) and not any(c in s for c in '{};()='):
            continue
        # Skip common rambling phrases if they don't look like code
        if re.match(r'^(I am|You can|How to|In this|This is|Please|Do you|Here is|Note:|The follow)', s) and not any(c in s for c in '{};()=.'):
            continue
        cleaned_lines.append(line)
    lines = cleaned_lines

    # Remove trailing truncated lines
    while lines:
        last_line = lines[-1].strip()
        if not last_line:
            lines = lines[:-1]
            continue
        
        is_truncated = False
        if re.search(r'[a-zA-Z0-9]$', last_line):
            if not last_line.endswith(';') and not last_line.endswith('{') and not last_line.endswith('}'):
                is_truncated = True
        
        if last_line.count('(') > last_line.count(')'):
            is_truncated = True
        if last_line.count('"') % 2 == 1:
            is_truncated = True
            
        truncated_keywords = ['import', 'public', 'private', 'protected', 'static', 'final', 'class', 'interface']
        for kw in truncated_keywords:
            if last_line.startswith(kw + ' ') and not last_line.endswith(';') and not last_line.endswith('{'):
                if '{' not in last_line:
                    is_truncated = True
                    break
        
        if is_truncated:
            lines = lines[:-1]
        else:
            break

    stripped = '\n'.join(lines).rstrip()

    # Balance braces
    open_braces = stripped.count('{')
    close_braces = stripped.count('}')

    if open_braces > close_braces:
        diff = open_braces - close_braces
        indent_level = 0
        for line in reversed(lines):
            if line.strip():
                match = re.match(r'^(\s*)', line)
                if match: indent_level = len(match.group(1))
                break
        for i in range(diff):
            indent = max(0, indent_level - (i * 4))
            stripped += '\n' + (' ' * indent) + '}'
    elif close_braces > open_braces:
        # If we have more closing braces, we might have junk after the class
        # Try to find where the top-level class definitely ends
        match = re.search(r'(public\s+)?(final\s+)?class\s+\w+', stripped)
        if match:
            start_pos = stripped.find('{', match.end())
            if start_pos != -1:
                brace_level = 1
                pos = start_pos + 1
                while pos < len(stripped) and brace_level > 0:
                    if stripped[pos] == '{': brace_level += 1
                    elif stripped[pos] == '}': brace_level -= 1
                    pos += 1
                if brace_level == 0:
                    # Truncate strictly after the class ends
                    stripped = stripped[:pos]

    return stripped

def strip_starcoder_tokens(code):
    """
    Strips Starcoder-specific special tokens from the code.
    """
    # Specific known starcoder tokens
    tokens = [
        '<|end|>', '<file_sep>', '<fim_prefix>', '<fim_suffix>',
        '<fim_middle>', '<|endoftext|>', '<|assistant|>', '<|system|>',
        '<|user|>', '<|endofcode|>', '<|end_of_code|>', '<|bot|>', '<|end|>',
        '<|begin_of_code_for_user|>', '<|thought|>', '<|getURL|>', '<|endoftext|>'
    ]
    for token in tokens:
        code = code.replace(token, '')

    # Generic tag stripping (e.g. <|any_tag|>)
    code = re.sub(r'<\|.*?\|>', '', code)

    # Also remove XML/HTML comments that often wrap junk in starcoder outputs
    # Improved to handle unclosed comments at the end of output
    code = re.sub(r'<!--.*?(?:-->|$)', '', code, flags=re.DOTALL)

    return code.strip()

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
        skip_until_non_boilerplate = False

        for i, line in enumerate(d_lines):
            ls = line.strip()
            if not ls:
                new_data_lines.append(line)
                continue

            # If it's a repeated import or package
            if (ls.startswith('import ') or ls.startswith('package ')) and ls in prompt_lines_set:
                continue

            # If it's a repeated class declaration - be more aggressive
            if re.match(r'^(public\s+)?(abstract\s+)?(final\s+)?class\s+\w+', ls):
                # Check if prompt already has a class declaration
                has_class_in_prompt = any(re.match(r'(public\s+)?(abstract\s+)?(final\s+)?class\s+\w+', p_line.strip())
                                         for p_line in p_lines)
                if has_class_in_prompt:
                    # This is a duplicate class definition, skip it and everything until we find useful code
                    skip_until_non_boilerplate = True
                    continue

            # Skip imports/packages that come after we detected a duplicate class
            if skip_until_non_boilerplate:
                if ls.startswith('import ') or ls.startswith('package ') or ls.startswith('/*') or ls.startswith('*') or ls.startswith('//'):
                    continue
                # Found actual code, stop skipping
                if ls and not ls.startswith('}'):
                    skip_until_non_boilerplate = False

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
    # Detect language
    is_java = item.get('_is_java_context', ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm')))
    
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
    # Add package declaration for Java if missing
    is_java = item.get('_is_java_context', ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm')))
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

def check_compilable_java(code):
    """
    Enhanced Java compilability check with multiple heuristics.
    """
    if not code or len(code.strip()) < 20:
        return False

    # Check brace balance
    if code.count('{') != code.count('}'):
        return False

    # Check parenthesis balance
    if code.count('(') != code.count(')'):
        return False

    # Check bracket balance
    if code.count('[') != code.count(']'):
        return False

    # Must have a class definition
    if not re.search(r'\b(class|interface|enum)\s+\w+', code):
        return False

    # Check for incomplete statements (line ending without terminator mid-code)
    lines = code.split('\n')
    for i, line in enumerate(lines[:-5] if len(lines) > 5 else []):  # Check all but last 5 lines
        stripped = line.strip()
        if stripped and not stripped.startswith('//') and not stripped.startswith('/*') and not stripped.startswith('*'):
            # Should end with proper terminator or control character
            if re.search(r'[a-zA-Z0-9]$', stripped):
                if not (stripped.endswith(';') or stripped.endswith('{') or stripped.endswith('}') or stripped.endswith(',')):
                    # Could be continuation, check next line
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        # If next line doesn't continue the statement, this is likely truncated
                        if next_line and not next_line.startswith('.') and not next_line.startswith('['):
                            return False

    # Check for misplaced imports (should be at top)
    in_class = False
    for line in lines:
        stripped = line.strip()
        if re.match(r'(public\s+)?(abstract\s+)?(final\s+)?class\s+\w+', stripped):
            in_class = True
        if in_class and stripped.startswith('import '):
            return False  # Import inside class body

    # Check for duplicate class definitions
    class_count = len(re.findall(r'\b(public\s+)?class\s+\w+', code))
    if class_count > 1:
        return False

    # Check for very short methods (likely truncated)
    method_pattern = r'(public|private|protected)\s+[\w<>[\]]+\s+\w+\s*\([^)]*\)\s*\{[^}]*\}'
    methods = re.findall(method_pattern, code, re.DOTALL)
    for method in methods:
        # Method body should have more than just whitespace
        body_match = re.search(r'\{([^}]*)\}', method, re.DOTALL)
        if body_match:
            body = body_match.group(1).strip()
            # Empty body is suspicious unless it's abstract
            if not body and 'abstract' not in method:
                # Empty methods are often signs of truncation/incompleteness
                pass  # Allow for now, as some prompts might have empty methods

    return True

def check_compilable(data):
    """
    Checks if code is compilable (Python or Java).
    """
    if not data or len(data.strip()) < 10:
        return False

    # Check for Java class structure
    if 'class ' in data and '{' in data:
        # Likely Java
        return check_compilable_java(data)

    # Try Python AST parse
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
    # Detect language
    is_java = item.get('_is_java_context', ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm')))
    
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
    # Detect language
    is_java = item.get('_is_java_context', ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm')))
    
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
    # Detect language
    is_java = item.get('_is_java_context', ('.java' in item.get('id', '').lower() or item.get('package', '').startswith('com.sallm')))
    
    data = strip_starcoder_tokens(data)
    
    extracted_data = extract_assistant_code(data)
    if extracted_data is not None:
        data = extracted_data
    # If no assistant tag found, we'll use the raw 'data' as-is
    
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
    jsonl_files = [f for f in files if f.endswith('.jsonl') and (f.startswith('github-dataset') or f.startswith('dataset'))]

    print(f"Found {len(jsonl_files)} files to process.")
    
    for filename in tqdm(jsonl_files):
        file_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        # Determine context from filename
        is_java_context = 'java' in filename.lower()
        
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    item = json.loads(line)
                    item['_is_java_context'] = is_java_context
                    data.append(item)
        
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
                if '_is_java_context' in item:
                    del item['_is_java_context']
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
                
    print("Processing complete.")

if __name__ == '__main__':
    main()
