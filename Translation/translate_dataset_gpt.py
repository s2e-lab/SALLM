# %%
from openai import OpenAI
import sys
import os
import json
from tqdm import tqdm
from datetime import datetime

# %%
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

with open(config_path) as f:
    config_data = json.loads(f.read())

OPENAI_KEY = config_data['OPENAI_KEY']
client = OpenAI(api_key=OPENAI_KEY)

model_name = "gpt-4o-mini-2024-07-18"

# %%
language_translation_codes = [
    # Afro-Asiatic
    ('Arabic', 'ara_Arab'),
    ('Hebrew', 'heb_Hebr'),
    # Austro-Asiatic
    ('Vietnamese', 'vie_Latn'),
    # Austronesian
    ('Indonesian', 'ind_Latn'),
    ('Malay', 'zlm_Latn'),
    ('Tagalog', 'tgl_Latn'),
    # Indo-European (Germanic)
    ('English', 'eng_Latn'),
    ('Dutch', 'nld_Latn'),
    ('German', 'deu_Latn'),
    ('Afrikaans', 'afr_Latn'),
    # Indo-European (Romance)
    ('Portuguese', 'por_Latn'),
    ('Spanish', 'spa_Latn'),
    ('French', 'fra_Latn'),
    ('Italian', 'ita_Latn'),
    # Indo-European (Greek)
    ('Greek', 'ell_Grek'),
    # Indo-European (Iranian)
    ('Persian', 'pes_Arab'),
    # Slavic
    ('Russian', 'rus_Cyrl'),
    ('Bulgarian', 'bul_Cyrl'),
    # Sino-Tibetan
    ('Chinese', 'zho_Hans'),
    # Turkic
    ('Turkish', 'tur_Latn'),
    # Uralic
    ('Estonian', 'est_Latn'),
    ('Finnish', 'fin_Latn'),
    ('Hungarian', 'hun_Latn'),
]

# %%
def gpt_response(text, from_lang, to_lang, temperature=0.2, max_tokens=512, n=1):
    try:
        if from_lang == 'English':
            system_message = f"You are a professional translator. Translate the following text from English to {to_lang}.\n"
        else:
            system_message = f"You are a professional translator. Translate the following text from {from_lang} to {to_lang}.\n"

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=0.95,
            n=n,
        )
        if n == 1:
            return response.choices[0].message.content.strip()
        else:
            return [choice.message.content.strip() for choice in response.choices]
    except Exception as e:
        print(f"[{datetime.now()}] Error during translation from {from_lang} to {to_lang}: {e}")
        return 'Problem occurred.'

# %%
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
        return json.load(infile)

def read_jsonl_file(file_path):
    json_data = []
    with open(file_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            if line.strip():
                json_data.append(json.loads(line))
    return json_data

# %%
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 32

def process_single_language(original_text, language):
    if language == 'English':
        return language, None
    
    # print(f"  [{datetime.now()}] Translating to {language} (10 candidates)...")
    candidates = gpt_response(original_text, 'English', language, n=10)
    
    if candidates == 'Problem occurred.':
        return language, 'Problem occurred.'

    lang_results = []
    for candidate in candidates:
        # Immediate back-translation
        back_trans = gpt_response(candidate, language, 'English', n=1)
        lang_results.append({
            'translation': candidate,
            'back_translation': back_trans
        })
    return language, lang_results

def process_translations(json_data, key):
    print(f"[{datetime.now()}] Processing 10 candidates + back-translations for key '{key}'...")

    updated_data = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for data in tqdm(json_data):
            if key in data and data[key]:
                original_text = data[key]
                translations_pool = {}
                
                future_to_lang = {
                    executor.submit(process_single_language, original_text, language): language 
                    for language, _ in language_translation_codes if language != 'English'
                }
                
                for future in as_completed(future_to_lang):
                    language, result = future.result()
                    if result:
                        translations_pool[language] = result
                
                data['translations_pool'] = translations_pool
            updated_data.append(data)

    print(f"[{datetime.now()}] Processed total records: {len(updated_data)}")
    return updated_data

# %%
def save_processed_data(json_data, new_filePath):
    print(f"[{datetime.now()}] Saving candidates pool to {new_filePath}")
    with open(new_filePath, 'w', encoding='utf-8') as outfile:
        for data in json_data:
            outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
    print(f"[{datetime.now()}] Data saved successfully.")

# %%
def process_file(file_path, key):
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    extension = os.path.splitext(file_path)[-1].lower()

    output_dir = "ProcessedFiles"
    os.makedirs(output_dir, exist_ok=True)
    
    new_filePath = os.path.join(output_dir, base_filename + '_candidates_raw' + extension)
    
    print(f"[{datetime.now()}] Reading {file_path}...")
    if extension == '.jsonl':
        json_data = read_jsonl_file(file_path)
    elif extension == '.json':
        json_data = read_json_file(file_path)
    else:
        print(f"Error: Unsupported file extension {extension}")
        return

    processed_data = process_translations(json_data, key)
    save_processed_data(processed_data, new_filePath)

# %%
def main():
    if len(sys.argv) < 3:
        print("Usage: python translate_dataset_gpt.py <file_path> <key>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]

    if not os.path.exists(file_path):
        # Try checking in ProcessedFiles if it doesn't exist relative to CWD
        alt_path = os.path.join("ProcessedFiles", os.path.basename(file_path))
        if os.path.exists(alt_path):
            file_path = alt_path
        else:
            print(f"Error: File {file_path} not found.")
            sys.exit(1)

    print(f"[{datetime.now()}] Input File: {file_path}, Key: {key}")
    process_file(file_path, key)

if __name__ == "__main__":
    main()



