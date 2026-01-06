#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 32     # Specify parallel environment and legal core size
#$ -q long          # Specify queue
#$ -N translate_java

python3 translate_dataset_gpt.py ../ProcessedFiles/dataset_java_nl_prompt.jsonl prompt_nl_prompt
