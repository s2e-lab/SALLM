#!/bin/bash

#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 1     # Specify parallel environment and legal core size
#$ -q long           # Specify queue
#$ -N  Salesforce_codegen-2B-mono



export PATH="/afs/crc.nd.edu/user/m/msiddiq3/Public/codeql-home/codeql:$PATH"
conda activate Franc
python evaluation.py