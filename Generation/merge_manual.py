import os
import json
import glob

output_dir = "/groups/jdasilv2/Latif/SALLM/Generation/Output"
base_names = [
    "dataset_java_nl_prompt_best",
    "github-dataset_java_nl_prompt_best"
]

for base_name in base_names:
    print(f"Checking for shards of {base_name} at temp 0.0...")
    pattern = os.path.join(output_dir, f"{base_name}_starcoder2_0.0_shard_*.jsonl")
    shard_files = glob.glob(pattern)
    
    if not shard_files:
        print(f"No shards found for {base_name}.")
        continue
        
    print(f"Found shards: {shard_files}")
    
    all_records = []
    for shard_file in shard_files:
        with open(shard_file, 'r', encoding='utf-8') as sf:
            for line in sf:
                if line.strip():
                    all_records.append(json.loads(line))
                    
    # Re-sort by original_idx to maintain original file order
    # Note: original_idx might be missing if it was old format, but Huggingface_model.py puts 'original_idx'
    try:
        all_records.sort(key=lambda x: x.get('original_idx', x.get('index_placeholder', 0)))
    except Exception as e:
        print("Could not sort by original_idx:", e)
        
    for r in all_records:
        r.pop('original_idx', None)
        r.pop('index_placeholder', None)

    output_file = os.path.join(output_dir, f"{base_name}_starcoder2_0.0.jsonl")
    print(f"Saving merged results to {output_file}")
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for record in all_records:
            out_f.write(json.dumps(record, ensure_ascii=False) + '\n')
            
    # Remove shards after successful merge
    for shard_file in shard_files:
        os.remove(shard_file)
        print(f"Deleted {shard_file}")
    
    print("-" * 40)
