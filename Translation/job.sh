#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 32     # Specify parallel environment and legal core size
#$ -q long          # Specify queue
#$ -N translate

conda activate app_testing
python translate_dataset_gpt.py
