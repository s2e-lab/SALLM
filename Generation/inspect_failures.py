import json
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'Filtered_Output')
    filename = 'dataset_nl_prompt_best_gemini-2.5-flash_0.0.jsonl'
    file_path = os.path.join(input_dir, filename)
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip(): continue
            try:
                item = json.loads(line)
                if 'generations' in item:
                    for lang, codes in item['generations'].items():
                        for obj in codes:
                            if not obj.get('compilable'):
                                print(f"--- Example {count+1} ---")
                                print(obj['cleared_code'])
                                print("-" * 20)
                                count += 1
                                if count >= 3:
                                    return
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
