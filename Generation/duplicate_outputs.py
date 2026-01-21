import json
import os

def duplicate_outputs(input_file, output_file, num_copies=10):
    """Duplicate each output entry 10 times."""
    data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    
    print(f"Processing {input_file}")
    print(f"Original items: {len(data)}")
    
    for item in data:
        if 'generations' in item and isinstance(item['generations'], dict):
            new_generations = {}
            for lang, codes in item['generations'].items():
                # Duplicate each code entry 10 times
                new_codes = []
                for code_entry in codes:
                    for _ in range(num_copies):
                        new_codes.append(code_entry)
                new_generations[lang] = new_codes
            item['generations'] = new_generations
    
    # Write back
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print(f"Written to {output_file}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filtered_dir = os.path.join(base_dir, 'Filtered_Output')
    
    # Files to process
    files_to_process = [
        'dataset_nl_prompt_best_qwen2.5_0.0.jsonl',
        'dataset_nl_prompt_best_starcoder2_0.0.jsonl',
        'dataset_java_nl_prompt_best_qwen2.5_0.0.jsonl',
        'dataset_java_nl_prompt_best_starcoder2_0.0.jsonl',
    ]
    
    for filename in files_to_process:
        file_path = os.path.join(filtered_dir, filename)
        if os.path.exists(file_path):
            duplicate_outputs(file_path, file_path, num_copies=10)
        else:
            print(f"File not found: {file_path}")
    
    print("Done!")

if __name__ == '__main__':
    main()
