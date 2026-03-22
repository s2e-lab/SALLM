#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 32
#$ -q long
#$ -N translate_all

# Translate all four datasets (standard + GitHub, Python + Java)
# Each generates 10 candidates per language with back-translations.

cd /groups/jdasilv2/Latif/SALLM/Translation

echo "[1/4] Translating Python standard dataset (100 prompts)..."
python3 translate_dataset_gpt.py ../ProcessedFiles/dataset_nl_prompt.jsonl prompt_nl_prompt

echo "[2/4] Translating Java standard dataset (100 prompts)..."
python3 translate_dataset_gpt.py ../ProcessedFiles/dataset_java_nl_prompt.jsonl prompt_nl_prompt

echo "[3/4] Translating GitHub Python dataset (25 prompts)..."
python3 translate_dataset_gpt.py ../ProcessedFiles/github-dataset_nl_prompt.jsonl prompt_nl_prompt

echo "[4/4] Translating GitHub Java dataset (25 prompts)..."
python3 translate_dataset_gpt.py ../ProcessedFiles/github-dataset_java_nl_prompt.jsonl prompt_nl_prompt

echo "Done. All candidate files written to ProcessedFiles/*_candidates_raw.jsonl"
