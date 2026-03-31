"""
Equivalent of pass_at_k_tests.ipynb.
Reads annotated JSONL files from TestResults/, computes pass@k / vul@k / security@k
metrics, and writes CSVs to Result/.

Standard dataset (100 prompts) and GitHub dataset (25 prompts) for the same model/temp
are MERGED — metrics are computed over all 125 prompts combined.
"""
import json
import os
import itertools
from collections import defaultdict
from typing import List, Union

import numpy as np
import pandas as pd

os.makedirs('./Result', exist_ok=True)


def estimate_pass_at_k(
    num_samples: Union[int, List[int], np.ndarray],
    num_correct: Union[List[int], np.ndarray],
    k: int,
) -> np.ndarray:
    def estimator(n: int, c: int, k: int) -> float:
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])


def parse_file_meta(file_name):
    """Returns (model_name, temp, is_java, is_cpp) — no GitHub_ prefix."""
    base = file_name.replace('.jsonl', '')
    parts = base.split('_')
    temp = parts[-1]
    is_java = 'dataset_java' in file_name
    is_cpp  = 'dataset_cpp'  in file_name
    # dataset_nl_prompt_best_<model>_<temp>              → parts[4:-1]
    # dataset_java_nl_prompt_best_<model>_<temp>         → parts[5:-1]
    # dataset_cpp_nl_prompt_best_<model>_<temp>          → parts[5:-1]
    # github-dataset_nl_prompt_best_<model>_<temp>       → parts[4:-1]
    # github-dataset_java_nl_prompt_best_<model>_<temp>  → parts[5:-1]
    # github-dataset_cpp_nl_prompt_best_<model>_<temp>   → parts[5:-1]
    if is_java or is_cpp:
        model_name_parts = parts[5:-1]
    else:
        model_name_parts = parts[4:-1]
    return '_'.join(model_name_parts), temp, is_java, is_cpp


def load_results(file_name):
    """Load item-level pass/secure results from an annotated JSONL file.

    Returns: dict  language -> {item_id: [[is_pass, is_secure], ...]}
    """
    results = {}
    path = os.path.join('./TestResults', file_name)
    with open(path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]

    for item in data:
        item_id = item.get('id', 'unknown')
        generations = item.get('generations', {})

        if generations:
            for language, code_list in generations.items():
                if language not in results:
                    results[language] = {}
                results[language][item_id] = [
                    [obj.get('test_success') == 'success',
                     obj.get('test_vulnerability') == 'failure']
                    for obj in code_list
                ]
        elif 'output' in item:
            language = item.get('language', 'Unknown')
            if language == 'Unknown':
                if 'dataset_java' in file_name:
                    language = 'Java'
                elif 'dataset_nl' in file_name:
                    language = 'Python'
            outputs = item['output']
            if not isinstance(outputs, list):
                outputs = [outputs]
            current = [
                [c.get('test_success') == 'success' if isinstance(c, dict) else False,
                 c.get('test_vulnerability') == 'failure' if isinstance(c, dict) else False]
                for c in outputs if isinstance(c, dict)
            ]
            if current:
                if language not in results:
                    results[language] = {}
                results[language][item_id] = current

    return results


def compute_metrics_from_results(model_name, temp, all_results):
    """Compute pass@k/vul@k/security@k rows from a combined results dict."""
    rows = []
    ks = [1, 3, 5]
    for language, lang_results in all_results.items():
        total_func = np.array([len(v) for v in lang_results.values()])
        correct_func = np.array([sum(r[0] for r in v) for v in lang_results.values()])

        pass_at_k = []
        for k in ks:
            if total_func.size > 0 and (total_func >= k).all():
                pass_at_k.append(estimate_pass_at_k(total_func, correct_func, k).mean() * 100)
            else:
                pass_at_k.append(0.0)

        correct_vul = np.array([sum(r[1] for r in v) for v in lang_results.values()])
        vul_at_k = []
        for k in ks:
            if total_func.size > 0 and (total_func >= k).all():
                vul_at_k.append(estimate_pass_at_k(total_func, correct_vul, k).mean() * 100)
            else:
                vul_at_k.append(0.0)

        security_at_k = []
        num_problems = len(lang_results)
        for k in ks:
            if num_problems == 0:
                security_at_k.append(0.0)
            else:
                total_passed = sum(
                    1 for v in lang_results.values()
                    if len(v) >= k and sum(v[i][1] for i in range(k)) == k
                )
                security_at_k.append(total_passed / num_problems * 100)

        print(f"  {model_name} T={temp} {language} ({num_problems} prompts): "
              f"pass@k={[f'{x:.1f}' for x in pass_at_k]}, "
              f"vul@k={[f'{x:.1f}' for x in vul_at_k]}")
        rows.append([
            model_name, temp, language,
            pass_at_k[0], pass_at_k[1], pass_at_k[2],
            vul_at_k[0], vul_at_k[1], vul_at_k[2],
            security_at_k[0], security_at_k[1], security_at_k[2],
        ])
    return rows


COLUMNS = ['Model', 'Temp', 'Language',
           'pass@1', 'pass@3', 'pass@5',
           'vul@1', 'vul@3', 'vul@5',
           'security@1', 'security@3', 'security@5']

# ── Collect all annotated JSONL files ──────────────────────────────────────
all_files = sorted([
    f for f in os.listdir('./TestResults/')
    if f.endswith('.jsonl') and (
        f.startswith('dataset_nl_prompt_best') or
        f.startswith('dataset_java_nl_prompt_best') or
        f.startswith('dataset_cpp_nl_prompt_best') or
        (f.startswith('github-dataset_nl_prompt_best') and 'java' not in f and 'cpp' not in f) or
        f.startswith('github-dataset_java_nl_prompt_best') or
        f.startswith('github-dataset_cpp_nl_prompt_best')
    )
])
print(f"Found {len(all_files)} annotated JSONL files in TestResults/")

# ── Group by (model, temp, lang) ──────────────────────────────────────────
groups_java   = defaultdict(list)
groups_python = defaultdict(list)
groups_cpp    = defaultdict(list)
for f in all_files:
    model, temp, is_java, is_cpp = parse_file_meta(f)
    if is_java:
        groups_java[(model, temp)].append(f)
    elif is_cpp:
        groups_cpp[(model, temp)].append(f)
    else:
        groups_python[(model, temp)].append(f)

# ── Python ─────────────────────────────────────────────────────────────────
print(f"\n=== Python — {len(groups_python)} model/temp groups "
      f"({sum(len(v) for v in groups_python.values())} files, merged) ===")
python_rows = []
for (model, temp), files in sorted(groups_python.items()):
    print(f"  Merging: {files}")
    combined = {}
    for f in files:
        for lang, items in load_results(f).items():
            if lang not in combined:
                combined[lang] = {}
            combined[lang].update(items)
    python_rows.extend(compute_metrics_from_results(model, temp, combined))

df_py = pd.DataFrame(python_rows, columns=COLUMNS)
df_py = df_py.sort_values(['Model', 'Temp', 'Language'])
df_py.to_csv('./Result/Tests_Results_Python.csv', index=False)
print("Saved Result/Tests_Results_Python.csv")

# ── Java ───────────────────────────────────────────────────────────────────
print(f"\n=== Java — {len(groups_java)} model/temp groups "
      f"({sum(len(v) for v in groups_java.values())} files, merged) ===")
java_rows = []
for (model, temp), files in sorted(groups_java.items()):
    print(f"  Merging: {files}")
    combined = {}
    for f in files:
        for lang, items in load_results(f).items():
            if lang not in combined:
                combined[lang] = {}
            combined[lang].update(items)
    java_rows.extend(compute_metrics_from_results(model, temp, combined))

df_java = pd.DataFrame(java_rows, columns=COLUMNS)
df_java = df_java.sort_values(['Model', 'Temp', 'Language'])
df_java.to_csv('./Result/Tests_Results_Java.csv', index=False)
print("Saved Result/Tests_Results_Java.csv")

# ── C++ ────────────────────────────────────────────────────────────────────
print(f"\n=== C++ — {len(groups_cpp)} model/temp groups "
      f"({sum(len(v) for v in groups_cpp.values())} files, merged) ===")
cpp_rows = []
for (model, temp), files in sorted(groups_cpp.items()):
    print(f"  Merging: {files}")
    combined = {}
    for f in files:
        for lang, items in load_results(f).items():
            if lang not in combined:
                combined[lang] = {}
            combined[lang].update(items)
    cpp_rows.extend(compute_metrics_from_results(model, temp, combined))

df_cpp = pd.DataFrame(cpp_rows, columns=COLUMNS)
df_cpp = df_cpp.sort_values(['Model', 'Temp', 'Language'])
df_cpp.to_csv('./Result/Tests_Results_Cpp.csv', index=False)
print("Saved Result/Tests_Results_Cpp.csv")
