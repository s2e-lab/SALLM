#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 1     # Specify parallel environment and legal core size
#$ -q gpu@@jung_gpu           # Specify queue
#$ -l gpu=2         # Specify queue
#$ -N  CodeGen2B

conda activate Franc
python CodeGen.py