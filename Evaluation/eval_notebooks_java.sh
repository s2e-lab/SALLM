#!/bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 4
#$ -q long
#$ -N eval_notebooks_java
#$ -cwd
source /afs/crc.nd.edu/x86_64_linux/Modules/4.7.0/init/bash

module load python/3.12.12

cd /groups/jdasilv2/Latif/SALLM/Evaluation

echo "[1/7] Running Test_Evaluation (annotating TestResults/ — Java + Python)..."
python3 run_test_evaluation.py

echo "[2/7] Running pass@k metrics (writing Result/ CSVs — Java + Python)..."
python3 run_pass_at_k.py

echo "[3/7] Running column_k_evaluation (language-family tables — Java + Python)..."
python3 column_k_evaluation.py

echo "[4/7] Running compilability analysis (Java + Python)..."
python3 analyze_compilability_result.py

echo "[5/7] Running Python vs Java comparison tables..."
python3 compare_python_java.py

echo "[6/7] Aggregating CodeQL results (Java)..."
python3 aggregate_codeql.py

echo "[7/7] Generating Result_Generation figures..."
cd ../Result_Generation
python3 generate_test_figures.py
python3 generate_compilation_figures.py
python3 generate_codeql_figures.py
cd ../Evaluation

echo "Done."
