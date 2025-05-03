# %%
from openai import OpenAI
from evaluate import load
import re
import sys
import os
import json
import warnings
from tqdm import tqdm

# %%
# from google.colab import drive
# drive.mount('/content/drive')
# %cd drive/My\ Drive/Colab\ Notebooks/Project_folder/FullPipeLine

# %%
with open("./config.json") as f:
    config_data = json.loads(f.read())



OPENAI_KEY = config_data['OPENAI_KEY']
client = OpenAI(api_key=OPENAI_KEY)

model_name = "gpt-4o-mini-2024-07-18"

# %% [markdown]
# **Defining language list**

# %%
language_translation_codes = [
    ('Acehnese', 'ace_Arab'),
    ('Hebrew', 'heb_Hebr'),
    ('Vietnamese', 'vie_Latn'),
    ('Indonesian', 'ind_Latn'),
    ('Malayalam', 'mal_Mlym'),
    ('Tagalog', 'tgl_Latn'),
    ('English', 'eng_Latn'),
    ('Dutch', 'nld_Latn'),
    ('German', 'deu_Latn'),
    ('Afrikaans', 'afr_Latn'),
    ('Portuguese', 'por_Latn'),
    ('Spanish', 'spa_Latn'),
    ('French', 'fra_Latn'),
    ('Italian', 'ita_Latn'),
    ('Greek', 'ell_Grek'),
    ('Western Persian', 'pes_Arab'),
    ('Russian', 'rus_Cyrl'),
    ('Bulgarian', 'bul_Cyrl'),
    ('Chinese', 'zho_Hans'),
    ('Turkish', 'tur_Latn'),
    ('Estonian', 'est_Latn'),
    ('Finnish', 'fin_Latn'),
    ('Spanish', 'spa_Latn'),
    ('Hungarian', 'hun_Latn'),
]


# %% [markdown]
# **Code** **starts**

# %%
def extract_docstrings(prompt):
    docstring_pattern = r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\''
    matches = re.findall(docstring_pattern, prompt)
    cleaned_matches = [match.strip('"""').strip("'''").strip() for match in matches]
    return ' | '.join(cleaned_matches) if cleaned_matches else ''

# %%
def gpt_4o_mini_response(prompt, from_lang, to_lang, temperature, max_tokens):
    # print("Translating from "+from_lang+" to "+to_lang)
    try:
        system_message = f"You are a translator. Translate the following sentence from {from_lang} to {to_lang}.\n"

        response = client.chat.completions.create(
            model= model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_message
                },
                {"role": "user", "content": prompt["prompt"]}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(e)
        return 'Problem occurred.'

# %%
gpt_4o_mini_response({"prompt": "How are you?"}, 'English', 'Bangla', 0.7, 128)

# %%
def read_json_file(file_path):
    print("File reading starts")

    with open(file_path, 'r') as infile:
        json_data = json.load(infile)

    print("File reading ends")
    return json_data


# %%
def read_jsonl_file(file_path):
    print("File reading starts")

    with open(file_path, 'r') as infile:
        lines = infile.readlines()

    json_data = [json.loads(line) for line in lines]
    print("File reading ends")

    return json_data

# %%
bertscore = load("bertscore")
def calculating_bertScore(references, predictions):
    # print("References: ")
    # print(references)
    # print("Predictions: ")
    # print(predictions)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        results = bertscore.compute(predictions=predictions, references=references, lang="en")

    return {key: results[key] for key in ['precision', 'recall', 'f1', 'hashcode']}

# %%

def process_translations(json_data, key):
    print("Processing translations...")

    new_columnName = 'translations'
    updated_data = []

    for data in tqdm(json_data):
    

        if key in data:
            key_value = data[key]
            # print("Key value: " + key_value)
            old_translation = data[new_columnName]

            translations = {}

            for lang, code in language_translation_codes:
                translations[lang] = []

                # print(len(old_translation[lang]))

                best_candidate = None
                best_bertscore = None
                best_back_translation = None

                for candidate in old_translation[lang]:
                    # print("Candidate: " + candidate)

                    # translate_key(key_value, code)

                    back_translation = gpt_4o_mini_response({"prompt": key_value}, lang, 'English', 0.7, 128)

                    bertscore_value = calculating_bertScore([key_value], [back_translation])

                    if best_candidate is None or bertscore_value['f1'][0] > best_bertscore['f1'][0]:
                        best_bertscore = bertscore_value
                        best_candidate = candidate
                        best_back_translation = back_translation

                translations[lang].append({
                        'translation': best_candidate,
                        'back_translation': best_back_translation,
                        'bertscore': best_bertscore
                    })
                    # print("************")
        else:
            translations = {lang: [] for lang, _ in language_translation_codes}

        data[new_columnName] = translations
        updated_data.append(data)
        # break

    print("Processed translations")
    return updated_data


# %%
def save_processed_data(json_data, new_filePath):
    # if os.path.exists(new_filePath):
    #     print(new_filePath+" already exists. No need to proceed.")
    #     return

    print("Saving processed data to "+new_filePath)
    with open(new_filePath, 'w', encoding='utf-8') as outfile:
        for data in json_data:
            outfile.write(json.dumps(data,ensure_ascii=False) + '\n')

    print("Processing completed. Data saved to "+new_filePath)



# %%
def process_file(file_path, key):
    base_filename = os.path.splitext(file_path)[0]
    extension = os.path.splitext(file_path)[-1].lower()

    print("Base name: "+base_filename+"Extension: "+extension)

    new_filePath = base_filename + '_gpt_nl_prompt_retranslated' + extension
    print("New file name: "+new_filePath)

    if extension != '.jsonl' and extension != '.json':
        print("Unsupported file extension")


    if extension == '.jsonl':
        json_data = read_jsonl_file(file_path)
    else:
        json_data = read_json_file(file_path)

    # print("****JSON DATA***")
    # print(json_data)
    processed_data = process_translations(json_data, key)
    save_processed_data(processed_data, new_filePath)

# %%
current_path = os.getcwd()

# Print it
print(f"Current working directory: {current_path}")
file_path = "./../Benchmarks/ProcessedFiles/sallm_nl_prompt_gpt_translated_prompt.jsonl"
key = "prompt_nl_prompt"

# Convert to absolute path to ensure correctness
file_path = os.path.abspath(file_path)

if not os.path.exists(file_path):
    print(f"Error: File {file_path} does not exist.")
    sys.exit(1)

print("file path: "+file_path+", key: "+key)

print("Starting file processing")
process_file(file_path, key)

# %%



