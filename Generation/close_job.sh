#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 32     # Specify parallel environment and legal core size
#$ -q long          # Specify queue
#$ -N close_job_gpt_githubpython
#$ -cwd             # Run in current directory

 python3 gpt_model.py ../ProcessedFiles/github-dataset_nl_prompt_best.jsonl


#export HF_HOME="/groups/jdasilv2/Latif/SALLM/.cache/huggingface"
#python3 gemini_model.py ../ProcessedFiles/github-dataset_nl_prompt_best.jsonl
