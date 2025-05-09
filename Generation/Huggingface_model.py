import os
import json
from tqdm import tqdm

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from datasets import load_dataset, Dataset

# Load dataset
dataset = load_dataset("s2e-lab/multi-SALLM")['train']

# Model choice
model_name = "bigcode/starcoder2-3b"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True,padding_side='left')
model = AutoModelForCausalLM.from_pretrained(
    model_name, trust_remote_code=True, device_map="auto", torch_dtype=torch.bfloat16
)


# Create text generation pipeline with explicit pad_token_id
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    torch_dtype=torch.bfloat16
)

generator.tokenizer.pad_token_id = generator.tokenizer.eos_token_id
# Create output directory
os.makedirs("Output", exist_ok=True)

# Prompt formatting
def create_prompt(item, key="prompt"):
    system_message = (
        f"You are an expert Python programmer and understand {item['language']}. Only output the code without any explanation."
    )
    user_message = item[key]
    return f"<|system|>\n{system_message}\n<|user|>\n{user_message}\n<|assistant|>\n"


# %%
def model_response(generator, prompt, temperature, max_tokens, key="prompt"):
    if temperature == 0.0:
        temperature = 1e-5

    try:

        # Generate outputs
        responses = generator(
            create_prompt(prompt, "translated_prompt"),
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

    with open(f"./Output/multi-dataset_starcoder2_{temp}.jsonl", 'w', encoding='utf-8') as f:
        for item in new_data:
            f.write(json.dumps(item,ensure_ascii=False) + '\n')

