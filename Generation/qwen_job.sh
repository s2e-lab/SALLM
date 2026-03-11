#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 4    # Specify parallel environment and legal core size
#$ -q long          # Specify queue
#$ -N qwen_generation
#$ -cwd

module load python/3.12.12

export HF_HOME="/groups/jdasilv2/Latif/SALLM/.cache/huggingface"
export PYTHONPATH="/groups/jdasilv2/Latif/SALLM/Generation/pypackages:$PYTHONPATH"

# Run for first file
python3 qwen_model.py ../ProcessedFiles/github-dataset_java_nl_prompt_best.jsonl

# Run for second file
python3 qwen_model.py ../ProcessedFiles/dataset_java_nl_prompt_best.jsonl
