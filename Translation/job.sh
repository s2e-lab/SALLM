#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 32
#$ -q long
#$ -N translate_cpp

# Translate all C++ datasets (standard + GitHub)
# Each generates 10 candidates per language with back-translations.

cd /groups/jdasilv2/Latif/SALLM/Translation

echo "[1/2] Translating CPP standard dataset (100 prompts)..."
python3 translate_dataset_gpt.py ../ProcessedFiles/dataset_cpp_nl_prompt.jsonl prompt_nl_prompt

echo "[2/2] Translating GitHub CPP dataset (25 prompts)..."
python3 translate_dataset_gpt.py ../ProcessedFiles/github-dataset_cpp_nl_prompt.jsonl prompt_nl_prompt

echo "Done. All candidate files written to ProcessedFiles/*_candidates_raw.jsonl"
