"""
Equivalent of repair_evaluation.ipynb.
Reads Filtered_Output JSONL files, computes compilability before/after repair,
and saves per-language CSVs to Result/.

  Result/compilation_results_Java.csv
  Result/compilation_results_Python.csv
  Result/compilation_results_Cpp.csv

Inspired by Generation/analyze_compilability.py.
"""
import json
import os
import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed

import pandas as pd

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR   = os.path.join(BASE_DIR, "..", "Generation", "Filtered_Output")
RESULT_DIR  = os.path.join(BASE_DIR, "Result")
os.makedirs(RESULT_DIR, exist_ok=True)

# Use the same strict checker from filter_code.py (handles Java brace balance,
# duplicate classes, misplaced imports, etc.) so that "before" and "after"
# are measured on the same scale.
sys.path.insert(0, os.path.join(BASE_DIR, "..", "Generation"))
from filter_code import check_compilable


def parse_filename(name_part):
    for prefix in (
        "github-dataset_java_nl_prompt_best_",
        "github-dataset_cpp_nl_prompt_best_",
        "github-dataset_nl_prompt_best_",
        "dataset_java_nl_prompt_best_",
        "dataset_cpp_nl_prompt_best_",
        "dataset_nl_prompt_best_",
    ):
        if name_part.startswith(prefix):
            remain = name_part[len(prefix):]
            is_java = "java" in prefix
            is_cpp  = "cpp"  in prefix
            if "_" in remain:
                model, temp = remain.rsplit("_", 1)
            else:
                model, temp = remain, "N/A"
            return model, temp, is_java, is_cpp
    return name_part, "N/A", False, False


def process_one_file(args):
    """
    Worker function to process a single JSONL file and return language-specific stats.
    """
    input_dir, filename = args
    name_part = filename.replace(".jsonl", "")
    model, temp, is_java, is_cpp = parse_filename(name_part)

    # Local stats for this file
    file_stats = {
        "java":   defaultdict(lambda: {"Total": 0, "Compilable_before": 0, "Compilable_after": 0}),
        "python": defaultdict(lambda: {"Total": 0, "Compilable_before": 0, "Compilable_after": 0}),
        "cpp":    defaultdict(lambda: {"Total": 0, "Compilable_before": 0, "Compilable_after": 0}),
    }

    if is_java:
        lang_key = "java"
    elif is_cpp:
        lang_key = "cpp"
    else:
        lang_key = "python"

    file_path = os.path.join(input_dir, filename)
    with open(file_path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue

            if "generations" in item and isinstance(item["generations"], dict):
                for lang, codes in item["generations"].items():
                    key = (model, temp, lang)
                    for obj in codes:
                        if not isinstance(obj, dict):
                            continue
                        file_stats[lang_key][key]["Total"] += 1
                        if check_compilable(obj.get("code", ""), is_java=is_java, is_cpp=is_cpp):
                            file_stats[lang_key][key]["Compilable_before"] += 1
                        if obj.get("compilable", False):
                            file_stats[lang_key][key]["Compilable_after"] += 1

            elif "output" in item and isinstance(item["output"], list):
                lang = item.get("language", "Unknown")
                key = (model, temp, lang)
                for obj in item["output"]:
                    if not isinstance(obj, dict):
                        continue
                    file_stats[lang_key][key]["Total"] += 1
                    if check_compilable(obj.get("code", ""), is_java=is_java, is_cpp=is_cpp):
                        file_stats[lang_key][key]["Compilable_before"] += 1
                    if obj.get("compilable", False):
                        file_stats[lang_key][key]["Compilable_after"] += 1

    # Convert defaultdict to regular dict for pickling (ProcessPoolExecutor restriction)
    for lang in file_stats:
        file_stats[lang] = {k: dict(v) for k, v in file_stats[lang].items()}
    return file_stats


def collect_data(input_dir):
    # Accumulate stats keyed by (model, temp, lang) so that standard + GitHub
    # files for the same model are merged into a single row (100 + 25 prompts).
    stats_java   = defaultdict(lambda: {"Total": 0, "Compilable_before": 0, "Compilable_after": 0})
    stats_python = defaultdict(lambda: {"Total": 0, "Compilable_before": 0, "Compilable_after": 0})
    stats_cpp    = defaultdict(lambda: {"Total": 0, "Compilable_before": 0, "Compilable_after": 0})

    files = sorted(f for f in os.listdir(input_dir) if f.endswith(".jsonl"))
    print(f"Found {len(files)} JSONL files in {input_dir}. Processing in parallel...")

    # Use ProcessPoolExecutor to speed up (C++ check starts a new g++ process every time)
    # Automatically uses all available CPU cores.
    with ProcessPoolExecutor(max_workers=32) as executor:
        futures = {executor.submit(process_one_file, (input_dir, f)): f for f in files}
        for future in as_completed(futures):
            filename = futures[future]
            try:
                file_results = future.result()
                # Merge stats
                for lang_key, data in file_results.items():
                    target = stats_java if lang_key == "java" else (stats_cpp if lang_key == "cpp" else stats_python)
                    for key, counts in data.items():
                        target[key]["Total"] += counts["Total"]
                        target[key]["Compilable_before"] += counts["Compilable_before"]
                        target[key]["Compilable_after"] += counts["Compilable_after"]
            except Exception as exc:
                print(f"File {filename} generated an exception: {exc}")

    def to_rows(stats):
        rows = []
        for (model, temp, lang), counts in sorted(stats.items()):
            total = counts["Total"]
            rows.append({
                "Model":                 model,
                "Temp":                  temp,
                "Language":              lang,
                "Total":                 total,
                "Compilable_before":     counts["Compilable_before"],
                "Compilable_after":      counts["Compilable_after"],
                "Compilable_before (%)": (counts["Compilable_before"] / total * 100) if total else 0,
                "Compilable_after (%)":  (counts["Compilable_after"]  / total * 100) if total else 0,
            })
        return rows

    return to_rows(stats_java), to_rows(stats_python), to_rows(stats_cpp)


def save(rows, label, path):
    df = pd.DataFrame(rows)
    if df.empty:
        print(f"No data for {label}, skipping.")
        return
    df = df.sort_values(["Model", "Temp", "Language"])
    df.to_csv(path, index=False)
    print(f"Saved {label} → {path}  ({len(df)} rows)")


def main():
    rows_java, rows_python, rows_cpp = collect_data(INPUT_DIR)
    save(rows_java,   "Java",   os.path.join(RESULT_DIR, "compilation_results_Java.csv"))
    save(rows_python, "Python", os.path.join(RESULT_DIR, "compilation_results_Python.csv"))
    save(rows_cpp,    "C++",    os.path.join(RESULT_DIR, "compilation_results_Cpp.csv"))


if __name__ == "__main__":
    main()
