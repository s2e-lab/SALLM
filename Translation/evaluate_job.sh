#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 4    # Specify parallel environment and legal core size
#$ -q gpu@@jung_gpu           # Specify queue
#$ -l gpu=2         # Specify queue
#$ -N evaluate_python

python3 evaluate_translations.py ../ProcessedFiles/dataset_nl_prompt_candidates_raw.jsonl prompt
