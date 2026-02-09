#!/bin/bash

#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 1     # Specify parallel environment and legal core size
#$ -q long           # Specify queue
#$ -N python_codeql_job

rm -rf ./Dataset/
export PATH="/groups/jdasilv2/Latif/codeql-home/codeql:$PATH"
# conda activate Franc
python 	codeql_job_runner.py
