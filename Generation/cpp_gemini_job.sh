#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 32
#$ -q long
#$ -N gen_all_cpp_gemini
#$ -cwd

# 1. Gemini-2.0-flash Generations (Currently using 2.5-flash as per script)
echo "Starting Gemini Generations..."
python3 gemini_model.py ../ProcessedFiles/dataset_cpp_nl_prompt_best.jsonl
python3 gemini_model.py ../ProcessedFiles/github-dataset_cpp_nl_prompt_best.jsonl

echo "Gemini Generation phase complete."
