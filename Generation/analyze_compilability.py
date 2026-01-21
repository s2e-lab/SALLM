import json
import os
import ast
from collections import defaultdict

def check_compilable(code):
    try:
        ast.parse(code)
        return True
    except:
        # Check for Java class structure heuristic
        if 'public class' in code or ('class ' in code and '{' in code and '}' in code):
            return True
        return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'Filtered_Output')
    
    if not os.path.exists(input_dir):
        print(f"Directory not found: {input_dir}")
        return

    files = [f for f in os.listdir(input_dir) if f.endswith('.jsonl')]
    
    # helper for stats: [before_success, before_total, after_success, after_total]
    # actually totals are same for before/after per file, so: [before_success, after_success, total_count]
    stats_python = defaultdict(lambda: [0, 0, 0])
    stats_java = defaultdict(lambda: [0, 0, 0])
    
    print(f"Analyzing {len(files)} files...")
    
    for filename in files:
        is_java = 'dataset_java' in filename
        current_stats = stats_java if is_java else stats_python
        
        name_part = filename.replace('.jsonl', '')
        if name_part.startswith('dataset_java_nl_prompt_best_'):
            remain = name_part.replace('dataset_java_nl_prompt_best_', '')
        elif name_part.startswith('dataset_nl_prompt_best_'):
            remain = name_part.replace('dataset_nl_prompt_best_', '')
        else:
            remain = name_part
            
        if '_' in remain:
            model, temp = remain.rsplit('_', 1)
        else:
            model = remain
            temp = "N/A"
            
        key = (model, temp)
        
        file_path = os.path.join(input_dir, filename)
        if not os.path.exists(file_path):
             print(f"File not found: {file_path}")
             continue
             
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): 
                    continue
                try:
                    item = json.loads(line)
                    if 'generations' in item and isinstance(item['generations'], dict):
                        for lang, codes in item['generations'].items():
                            for output_obj in codes:
                                if isinstance(output_obj, dict):
                                    original_code = output_obj.get('code', '')
                                    after_compilable = output_obj.get('compilable', False)
                                    before_compilable = check_compilable(original_code)
                                    
                                    current_stats[key][0] += 1 if before_compilable else 0
                                    current_stats[key][1] += 1 if after_compilable else 0
                                    current_stats[key][2] += 1
                                else:
                                    pass
                    elif 'output' in item and isinstance(item['output'], list):
                        for output_obj in item['output']:
                                if isinstance(output_obj, dict):
                                    original_code = output_obj.get('code', '')
                                    after_compilable = output_obj.get('compilable', False)
                                    before_compilable = check_compilable(original_code)
                                    current_stats[key][0] += 1 if before_compilable else 0
                                    current_stats[key][1] += 1 if after_compilable else 0
                                    current_stats[key][2] += 1
                    else:
                        pass
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in {filename}")
                    pass

    # Print tables
    def print_table(title, stats_dict):
        print(f"\n# {title} Analysis")
        header = f"{'Model':<20} | {'Temp':<5} | {'Before %':<10} | {'After %':<10} | {'Delta %':<10} | {'Samples':<8}"
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        
        sorted_keys = sorted(stats_dict.keys())
        
        for model, temp in sorted_keys:
            before, after, total = stats_dict[(model, temp)]
            if total == 0:
                continue
                
            before_pct = (before / total) * 100
            after_pct = (after / total) * 100
            delta = after_pct - before_pct
            
            print(f"{model:<20} | {temp:<5} | {before_pct:<10.2f} | {after_pct:<10.2f} | {delta:<10.2f} | {total:<8}")

    print_table("Python", stats_python)
    print_table("Java", stats_java)

if __name__ == "__main__":
    main()
