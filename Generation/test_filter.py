import json
import os
import sys

# Import functions from filter_code.py
sys.path.append(os.getcwd())
try:
    from filter_code import check_compilable_cpp, process_item, clear_generated_code_gpt
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

# Load one sample from a GPT-4o-mini C++ JSONL
test_file = 'Output/dataset_cpp_nl_prompt_best_gpt-4o-mini_0.0.jsonl'
if not os.path.exists(test_file):
    print(f"Test file {test_file} not found.")
    sys.exit(1)

with open(test_file, 'r') as f:
    line = f.readline()
    if not line:
        print("Empty test file.")
        sys.exit(1)
    item = json.loads(line)

print(f"Testing 1 sample (22 languages) for C++ parallel filtering...")
import time
start = time.time()

# Mock the parameters
cleaner_func = clear_generated_code_gpt
is_java_context = False
is_cpp_context = True

# Process the item
processed_item = process_item(item, cleaner_func, is_java_context, is_cpp_context)
end = time.time()

print(f"Processed item in {end - start:.2f} seconds.")
print(f"Compilability results: {len(processed_item['generations'])} languages processed.")
