# %%
import json
import openai
from tqdm import tqdm
import time


# %%
with open("./config.json") as f:
    config_data = json.loads(f.read())

OPENAI_KEY = config_data['OPENAI_KEY']
openai.api_key = OPENAI_KEY
print(OPENAI_KEY)

model_name = "gpt-4"



# %%
def gpt_response(prompt, temperature, max_tokens):
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt["prompt"]+'\n'
                }
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n=10,
        )
        prompt['output'] = response
        time.sleep(10)
        return prompt
    except Exception as e:
        print(e)
        prompt['output'] = 'Problem occurred.'
        return prompt



# %%
with open('./Output/dataset_gpt-4_1.0.jsonl', 'r') as f:
    data = [json.loads(line) for line in f.readlines()]

print(len(data))

# %%
for temp in [1.0]:
    print(f"Temperature: {temp}")

    for i in tqdm(range(len(data))):
        id = data[i]['id']
        output = data[i]['output']
        if not "Problem occurred." in output:
            continue
        print(f"ID: {id}")
        data[i] = gpt_response(data[i], temp, 512)

    
    with open(f"./Output/x_dataset_{model_name.replace('/','_')}_{temp}.jsonl", 'w') as f:
        for line in data:
            f.write(json.dumps(line) + '\n')

# %%
