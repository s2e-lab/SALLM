#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 4
#$ -q long
#$ -N eval_notebooks_cpp
#$ -cwd
#$ -hold_jid 766841
source /afs/crc.nd.edu/x86_64_linux/Modules/4.7.0/init/bash

module load python/3.12.12

cd /groups/jdasilv2/Latif/SALLM/Evaluation

echo "[1/5] Annotating test results (C++)..."
python3 run_test_evaluation.py

echo "[2/5] Running pass@k metrics (C++)..."
python3 run_pass_at_k.py

echo "[3/5] Running column_k language-family tables (C++)..."
python3 column_k_evaluation.py

echo "[4/5] Running compilability analysis (C++)..."
python3 analyze_compilability_result.py

echo "[5/5] Aggregating CodeQL + generating figures..."
python3 aggregate_codeql.py
cd ../Result_Generation
python3 generate_test_figures.py
python3 generate_compilation_figures.py
python3 generate_codeql_figures.py
cd ../Evaluation

echo "Done."
