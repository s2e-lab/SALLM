# %%
from evaluate import load
import sys
import os
import json
import warnings
from tqdm import tqdm
from datetime import datetime

# %%
import threading

# Load BERTScore metric
bertscore = load("bertscore")
bert_lock = threading.Lock()

def calculating_bertScore(references, predictions):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # Use a smaller, faster model (distilbert-base-uncased)
        with bert_lock:
            results = bertscore.compute(
                predictions=predictions, 
                references=references, 
                lang="en", 
                model_type="distilbert-base-uncased"
            )
    return {key: results[key] for key in ['precision', 'recall', 'f1', 'hashcode']}

# %%
def read_jsonl_file(file_path):
    json_data = []
    with open(file_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            if line.strip():
                json_data.append(json.loads(line))
    return json_data

def save_processed_data(json_data, new_filePath):
    print(f"[{datetime.now()}] Saving best translations to {new_filePath}")
    with open(new_filePath, 'w', encoding='utf-8') as outfile:
        for data in json_data:
            outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
    print(f"[{datetime.now()}] Data saved successfully.")

# %%
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 4

def evaluate_single_language(original_english, lang, candidates):
    if candidates == 'Problem occurred.':
        return lang, 'Problem occurred.'
    
    if not candidates:
        return lang, None

    # Prepare references and predictions for batch BERTScore calculation
    references = [original_english] * len(candidates)
    predictions = [c['back_translation'] for c in candidates]
    
    # Filter out candidates with failed back-translations
    valid_indices = [i for i, p in enumerate(predictions) if p != 'Problem occurred.']
    if not valid_indices:
        return lang, 'Problem occurred.'
    
    valid_refs = [references[i] for i in valid_indices]
    valid_preds = [predictions[i] for i in valid_indices]
    
    scores = calculating_bertScore(valid_refs, valid_preds)
    
    # Find index with highest F1
    max_f1 = -1
    best_idx_in_valid = -1
    for i, f1 in enumerate(scores['f1']):
        if f1 > max_f1:
            max_f1 = f1
            best_idx_in_valid = i
    
    original_idx = valid_indices[best_idx_in_valid]
    best_cand = candidates[original_idx]
    
    result = {
        'translation': best_cand['translation'],
        'back_translation': best_cand['back_translation'],
        'bertscore': {
            'precision': float(scores['precision'][best_idx_in_valid]),
            'recall': float(scores['recall'][best_idx_in_valid]),
            'f1': float(scores['f1'][best_idx_in_valid])
        }
    }
    return lang, result

def evaluate_and_select_best(json_data, key):
    print(f"[{datetime.now()}] Evaluating candidates using BERTScore for key '{key}'...")

    updated_data = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for data in tqdm(json_data):
            if 'translations_pool' in data:
                original_english = data[key]
                pool = data['translations_pool']
                best_translations = {}

                future_to_lang = {
                    executor.submit(evaluate_single_language, original_english, lang, candidates): lang 
                    for lang, candidates in pool.items()
                }
                
                for future in as_completed(future_to_lang):
                    lang, result = future.result()
                    if result:
                        best_translations[lang] = result
                
                data['translations'] = best_translations
            
            updated_data.append(data)
    
    return updated_data

# %%
def process_file(file_path, key):
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    extension = os.path.splitext(file_path)[-1].lower()

    # If the input was '_candidates_raw', strip it for the output
    if base_filename.endswith('_candidates_raw'):
        base_filename = base_filename[:-15]

    output_dir = "../ProcessedFiles"
    os.makedirs(output_dir, exist_ok=True)
    
    new_filePath = os.path.join(output_dir, base_filename + '_best' + extension)
    
    print(f"[{datetime.now()}] Reading {file_path}...")
    json_data = read_jsonl_file(file_path)

    processed_data = evaluate_and_select_best(json_data, key)
    save_processed_data(processed_data, new_filePath)

# %%
def main():
    if len(sys.argv) < 3:
        print("Usage: python evaluate_translations.py <raw_candidates_file> <original_key>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]

    if not os.path.exists(file_path):
        # Check in ProcessedFiles
        alt_path = os.path.join("ProcessedFiles", os.path.basename(file_path))
        if os.path.exists(alt_path):
            file_path = alt_path
        else:
            print(f"Error: File {file_path} not found.")
            sys.exit(1)

    print(f"[{datetime.now()}] Input Raw File: {file_path}, Key: {key}")
    process_file(file_path, key)

if __name__ == "__main__":
    main()
