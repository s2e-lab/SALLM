# %%
import json
import openai
from tqdm import tqdm
import time
from openai import OpenAI



# %%
with open("./config.json") as f:
    config_data = json.loads(f.read())

OPENAI_KEY = config_data['OPENAI_KEY']
client = OpenAI(api_key=OPENAI_KEY)
model_name = "gpt-4o-mini-2024-07-18"



# %%
def gpt_response(prompt, temperature, max_tokens, key="prompt"):
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert Python programmer and understand {prompt['language']}. Only output the code without any explanation. "
                },
                {
                    "role": "user",
                    "content": prompt[key]+'\n'
                }
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n=10,
        )
        prompt['output'] = []
        for choice in response.choices:
            prompt['output'].append(choice.message.content.strip())
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
        item = gpt_response(item, temp, 512,"translated_prompt")
        # print(item)
        new_data.append(item)

        # break

    with open(f"./Output/multi-dataset_gpt-4o-mini_{temp}.jsonl", 'w', encoding='utf-8') as f:
        for item in new_data:
            f.write(json.dumps(item,ensure_ascii=False) + '\n')

# %%
