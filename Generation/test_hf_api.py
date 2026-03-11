import os
import json
from openai import OpenAI

config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path, 'r') as f:
    config = json.load(f)

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=config["HF_TOKEN"],
)

model = "Qwen/Qwen2.5-Coder-3B-Instruct"

try:
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
        max_tokens=10,
        temperature=0.0,
        n=10
    )
    print("Success, choices length:", len(completion.choices))
except Exception as e:
    print("Error:", e)
