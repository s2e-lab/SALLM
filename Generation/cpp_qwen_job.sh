#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 4
#$ -q long
#$ -N gen_all_cpp_qwen
#$ -cwd

module load python/3.12.12

export HF_HOME="/groups/jdasilv2/Latif/SALLM/.cache/huggingface"
export PYTHONPATH="/groups/jdasilv2/Latif/SALLM/Generation/pypackages:$PYTHONPATH"

# 1. Qwen-Coder-3B Generations
echo "Starting Qwen-Coder-3B Generations..."
python3 qwen_model.py ../ProcessedFiles/dataset_cpp_nl_prompt_best.jsonl
python3 qwen_model.py ../ProcessedFiles/github-dataset_cpp_nl_prompt_best.jsonl

echo "Qwen Generation phase complete."
