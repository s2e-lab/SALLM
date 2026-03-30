import json
import csv
import os

input_file = '/groups/jdasilv2/Latif/SALLM/ProcessedFiles/dataset_nl_prompt_best.jsonl'
output_file = '/groups/jdasilv2/Latif/SALLM/Translation/Translation_Evaluation.csv'

# Select first 5 samples
samples = []
with open(input_file, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i >= 5:
            break
        samples.append(json.loads(line))

# Header
header = [
    'Language', 
    'Sample ID', 
    'English (Original)', 
    'Translation', 
    'Back-Translation', 
    'BERTScore Precision',
    'BERTScore Recall',
    'BERTScore F1',
    'Naturalness (1-5)', 
    'Expressiveness (1-5)', 
    'Adequacy (1-5)', 
    'Conciseness (1-5)',
    'Comments'
]

# Write CSV
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
    # Sort languages for better readability
    all_langs = sorted(list(samples[0]['translations'].keys()))
    
    for lang in all_langs:
        for sample in samples:
            original = sample.get('prompt_nl_prompt', '')
            trans_data = sample['translations'].get(lang, {})
            
            translation = trans_data.get('translation', 'N/A')
            back_translation = trans_data.get('back_translation', 'N/A')
            bert = trans_data.get('bertscore', {})
            
            writer.writerow([
                lang,
                sample.get('id', 'N/A'),
                original,
                translation,
                back_translation,
                bert.get('precision', 'N/A'),
                bert.get('recall', 'N/A'),
                bert.get('f1', 'N/A'),
                '', # Naturalness
                '', # Expressiveness
                '', # Adequacy
                '', # Conciseness
                ''  # Comments
            ])

print(f"Created evaluation sheet with {len(all_langs) * len(samples)} entries.")
