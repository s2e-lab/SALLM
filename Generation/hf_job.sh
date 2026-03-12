#!/bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 4    # Specify parallel environment and legal core size
#$ -q gpu@@jung_gpu         # Specify queue
#$ -l gpu=4        # Specify queue
#$ -N starcoder_java
#$ -cwd

module load python/3.12.12

export HF_HOME="/groups/jdasilv2/Latif/SALLM/.cache/huggingface"
export PYTHONPATH="/groups/jdasilv2/Latif/SALLM/Generation/pypackages:$PYTHONPATH"
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True"

python3 Huggingface_model.py ../ProcessedFiles/dataset_java_nl_prompt_best.jsonl
