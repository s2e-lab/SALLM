import json
import os
import argparse
from collections import defaultdict
from filter_code import check_compilable

def print_table(title, stats_dict):
    print(f"\n# {title} Analysis")
    header = f"{'Model':<40} | {'Temp':<5} | {'Before %':<10} | {'After %':<10} | {'Delta %':<10} | {'Samples':<8}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for model, temp in sorted(stats_dict.keys()):
        before, after, total = stats_dict[(model, temp)]
        if total == 0:
            continue
        before_pct = (before / total) * 100
        after_pct = (after / total) * 100
        delta = after_pct - before_pct
        print(f"{model:<40} | {temp:<5} | {before_pct:<10.2f} | {after_pct:<10.2f} | {delta:<10.2f} | {total:<8}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default=None, help='Filter files by model name (e.g. gpt, gemini)')
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, 'Filtered_Output')

    if not os.path.exists(input_dir):
        print(f"Directory not found: {input_dir}")
        return

    files = [
        f for f in os.listdir(input_dir)
        if f.endswith('.jsonl') and 'cpp' in f.lower()
    ]

    if args.model:
        files = [f for f in files if args.model.lower() in f.lower()]

    print(f"Analyzing {len(files)} files...")

    stats_cpp = defaultdict(lambda: [0, 0, 0])
    stats_github_cpp = defaultdict(lambda: [0, 0, 0])

    for filename in files:
        is_cpp = 'cpp' in filename.lower()
        is_github = 'github-dataset' in filename

        current_stats = stats_github_cpp if is_github else stats_cpp

        name_part = filename.replace('.jsonl', '')
        if name_part.startswith('dataset_cpp_nl_prompt_best_'):
            remain = name_part.replace('dataset_cpp_nl_prompt_best_', '')
        elif name_part.startswith('github-dataset_cpp_nl_prompt_best_'):
            remain = name_part.replace('github-dataset_cpp_nl_prompt_best_', '')
        else:
            remain = name_part

        if '_' in remain:
            model, temp = remain.rsplit('_', 1)
        else:
            model = remain
            temp = "N/A"

        key = (model, temp)

        file_path = os.path.join(input_dir, filename)
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
                                    before_compilable = check_compilable(original_code, is_cpp=is_cpp)
                                    current_stats[key][0] += 1 if before_compilable else 0
                                    current_stats[key][1] += 1 if after_compilable else 0
                                    current_stats[key][2] += 1
                    elif 'output' in item and isinstance(item['output'], list):
                        for output_obj in item['output']:
                            if isinstance(output_obj, dict):
                                original_code = output_obj.get('code', '')
                                after_compilable = output_obj.get('compilable', False)
                                before_compilable = check_compilable(original_code, is_cpp=is_cpp)
                                current_stats[key][0] += 1 if before_compilable else 0
                                current_stats[key][1] += 1 if after_compilable else 0
                                current_stats[key][2] += 1
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in {filename}")

    print_table("Standard C++", stats_cpp)
    print_table("GitHub C++", stats_github_cpp)

if __name__ == "__main__":
    main()
