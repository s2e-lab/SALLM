#!/bin/bash

#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe               # Send mail when job begins, ends and aborts
#$ -pe smp 16           # Specify parallel environment and legal core size
#$ -q long              # Specify queue
#$ -l h=d32cepyc*      # Target d32 nodes only
#$ -N codeql_cpp_gemini
#$ -cwd                 # Run in current directory

source /afs/crc.nd.edu/x86_64_linux/Modules/4.7.0/init/bash

module load python/3.12.12

cd /groups/jdasilv2/Latif/SALLM/Evaluation

export PATH="/groups/jdasilv2/Latif/codeql-home/codeql:$PATH"
python3 codeql_job_runner.py --mode cpp_gemini
