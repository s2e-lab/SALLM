#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 4    # Specify parallel environment and legal core size
#$ -q gpu@@jung_gpu           # Specify queue
#$ -l gpu=2         # Specify queue
#$ -N starcoder_java

python Huggingface_model.py ../ProcessedFiles/dataset_java_nl_prompt_best.jsonl
