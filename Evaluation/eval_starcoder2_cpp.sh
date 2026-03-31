#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe               # Send mail when job begins, ends and aborts
#$ -pe smp 64           # Specify parallel environment and legal core size
#$ -q long              # Specify queue
#$ -N eval_starcoder2_cpp
#$ -cwd                 # Run in current directory
#$ -hold_jid 766831     # Wait for filter job to finish

source /afs/crc.nd.edu/x86_64_linux/Modules/4.7.0/init/bash

module load python/3.12.12

cd /groups/jdasilv2/Latif/SALLM/Evaluation

python3 run_tests_singularity.py --model starcoder2 --lang cpp --no-github
