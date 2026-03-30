#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 32
#$ -q long
#$ -N gen_all_cpp
#$ -cwd

# 1. GPT-4o-mini Generations
echo "Starting GPT-4o-mini Generations..."
python3 gpt_model.py ../ProcessedFiles/dataset_cpp_nl_prompt_best.jsonl
python3 gpt_model.py ../ProcessedFiles/github-dataset_cpp_nl_prompt_best.jsonl

echo "GPT Generation phase complete."
