# %%
import json
import openai
from tqdm import tqdm
import time
from google import genai
from google.genai import types




# %%
with open("./config.json") as f:
    config_data = json.loads(f.read())

GEMINI_KEY = config_data['GEMINI_KEY']
client =genai.Client(api_key=GEMINI_KEY)
# model_name = "gemini-2.5-flash-preview-04-17"
model_name = "gemini-2.0-flash"



# %%
def gemini_response(prompt, temperature, max_tokens, key="prompt"):
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=[prompt[key]+'\n'],
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
                candidate_count = 8,
                presence_penalty=0,
                frequency_penalty=0,
                system_instruction=f"You are an expert Python programmer and understand {prompt['language']}. Only output the code without any explanation."
        
            ),
        )
        prompt['output'] = []
        for choice in response.candidates:
            prompt['output'].append(choice.content.parts[0].text.strip())
        time.sleep(1)
        return prompt
    except Exception as e:
        print(e)
        prompt['output'] = 'Problem occurred.'
        return prompt



# %%
from datasets import load_dataset

dataset = load_dataset("s2e-lab/multi-SALLM")
dataset = dataset['train']

# %%
for temp in [0.0, 0.2, 0.4, 0.6,0.8,1.0]:
    print(f"Temperature: {temp}")
    new_data =[]
    for i in tqdm(range(len(dataset))):
        item = dataset[i]
        item = gemini_response(item, temp, 512,"translated_prompt")
        # print(item)
        new_data.append(item)

        # break

    with open(f"./Output/multi-dataset_gemini-2.5-flash_{temp}.jsonl", 'w', encoding='utf-8') as f:
        for item in new_data:
            f.write(json.dumps(item,ensure_ascii=False) + '\n')

    # break

# %%
