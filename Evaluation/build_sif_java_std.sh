#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe               # Send mail when job begins, ends and aborts
#$ -pe smp 4            # Specify parallel environment and legal core size
#$ -q long              # Specify queue
#$ -N build_sif_java_std
#$ -cwd                 # Run in current directory

module load python/3.12.12

cd /groups/jdasilv2/Latif/SALLM/Evaluation

# Stage 1: build base SIF (downloads Maven deps — takes ~5-10 min)
# Stage 2: build 100 per-item SIFs (--jobs 1 to avoid localimage race condition)
python3 build_sif_fakeroot.py --lang java-std --jobs 1
