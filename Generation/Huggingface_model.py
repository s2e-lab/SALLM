# %%
import os
import json
from tqdm import tqdm


# %%
from transformers import pipeline

# %%
from datasets import load_dataset

dataset = load_dataset("s2e-lab/multi-SALLM")
dataset = dataset['train']

# %%
model_name = "Qwen/Qwen2.5-Coder-0.5B"

# %%
generator = pipeline("text-generation", model = model_name,  trust_remote_code=True)

# %%
def model_response(generator, prompt, temperature, max_tokens, key="prompt"):
    if temperature == 0.0:
        temperature = 1e-5

    try:
        system_message = f"You are an expert Python programmer and understand {prompt['language']}. Only output the code without any explanation."
        user_message = prompt[key]

        # Combine system and user message into a single prompt
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

        # Generate outputs
        responses = generator(
            messages,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_p=1.0,
            num_return_sequences=10,
            do_sample=True
        )

        prompt['output'] = []
        for resp in responses:
          if 'generated_text' in resp and len(resp['generated_text']) == 3:
            prompt['output'].append(resp['generated_text'][2]['content'].strip())

        return prompt

    except Exception as e:
        print(e)
        prompt['output'] = 'Problem occurred.'
        return prompt

# %%
for temp in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    print("Temperature: {temp}")
    new_data = []
    for item in tqdm(dataset):
        item = model_response(generator, item, temp, 512, "translated_prompt")

        new_data.append(item)

    with open(f"./Output/multi-dataset-Qwen_{temp}.jsonl", 'w', encoding='utf-8') as f:
        for item in new_data:
            f.write(json.dumps(item,ensure_ascii=False) + '\n')

# %% [markdown]
# 


