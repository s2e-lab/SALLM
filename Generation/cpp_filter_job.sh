#!/bin/bash
#$ -S /bin/bash
#$ -pe smp 32
#$ -q long
#$ -N filter_cpp_gpt
#$ -cwd
#$ -V
#$ -l h_rt=04:00:00

if ! command -v module &> /dev/null; then
    if [ -f /etc/profile.d/modules.sh ]; then
        . /etc/profile.d/modules.sh
    fi
fi

module load python/3.12.12
export PYTHONPATH="$PWD/pypackages:$PYTHONPATH"

echo "Starting Parallel C++ Filtering and Analysis (GPT only)..."
python3 filter_code.py --model gpt
# python3 analyze_compilability.py --model gpt

echo "C++ Filtering and Analysis complete."
