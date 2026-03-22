#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 4
#$ -q gpu@@jung_gpu
#$ -l gpu=2
#$ -N evaluate_all

# Select best translation candidate per language using BERTScore (back-translation F1).
# Key must be prompt_nl_prompt — the extracted docstring used as the translation source.

cd /groups/jdasilv2/Latif/SALLM/Translation

echo "[1/4] Evaluating Python standard dataset (100 prompts)..."
python3 evaluate_translations.py ../ProcessedFiles/dataset_nl_prompt_candidates_raw.jsonl prompt_nl_prompt

echo "[2/4] Evaluating Java standard dataset (100 prompts)..."
python3 evaluate_translations.py ../ProcessedFiles/dataset_java_nl_prompt_candidates_raw.jsonl prompt_nl_prompt

echo "[3/4] Evaluating GitHub Python dataset (25 prompts)..."
python3 evaluate_translations.py ../ProcessedFiles/github-dataset_nl_prompt_candidates_raw.jsonl prompt_nl_prompt

echo "[4/4] Evaluating GitHub Java dataset (25 prompts)..."
python3 evaluate_translations.py ../ProcessedFiles/github-dataset_java_nl_prompt_candidates_raw.jsonl prompt_nl_prompt

echo "Done. Best translations written to ProcessedFiles/*_best.jsonl"
