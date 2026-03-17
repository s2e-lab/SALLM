#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe               # Send mail when job begins, ends and aborts
#$ -pe smp 4            # Specify parallel environment and legal core size
#$ -q long              # Specify queue
#$ -N build_sif_python_dataset
#$ -cwd                 # Run in current directory

module load python/3.12.12

cd /groups/jdasilv2/Latif/SALLM/Evaluation

python3 build_sif_fakeroot.py --lang python-dataset --jobs 4
