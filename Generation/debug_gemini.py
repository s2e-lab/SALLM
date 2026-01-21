import json
import os

def get_last_function_name_from_code(code):
    """
    Extracts the function name from the given code string.
    """
    # Split the code into lines
    lines = code.split('\n')
    
    # Iterate through each line to find the function definition
    for line in lines:
        if line.strip().startswith('def '):
            # Extract the function name
            function_name = line.split('(')[0].replace('def ', '').strip()
            return "def "+function_name+'('
    
    return None

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'Filtered_Output')
    filename = 'dataset_nl_prompt_best_gemini-2.5-flash_0.0.jsonl'
    file_path = os.path.join(input_dir, filename)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= 3: break # check first 3
            item = json.loads(line)
            prompt = item['prompt'] if 'prompt' in item else item.get('translated_prompt', '')
            
            print(f"--- Item {i+1} ---")
            print(f"Prompt end snippet:\n{prompt[-100:]}")
            func_name = get_last_function_name_from_code(prompt)
            print(f"Extracted function name: '{func_name}'")
            print("-" * 20)

if __name__ == '__main__':
    main()
