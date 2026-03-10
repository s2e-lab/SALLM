#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe               # Send mail when job begins, ends and aborts
#$ -pe smp 32           # Specify parallel environment and legal core size
#$ -q long              # Specify queue
#$ -N eval_gpt_java
#$ -cwd                 # Run in current directory

module load python/3.12.12

cd /groups/jdasilv2/Latif/SALLM/Evaluation

python3 run_tests_singularity.py --model gpt --lang Java --no-github
