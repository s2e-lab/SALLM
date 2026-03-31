#!/bin/bash
#$ -S /bin/bash
#$ -M msiddiq3@nd.edu
#$ -m abe
#$ -pe smp 4
#$ -q gpu
#$ -l gpu=1
#$ -N ollama_cpp_06
#$ -cwd
#$ -V
#$ -l h_rt=72:00:00

if ! command -v module &> /dev/null; then
    if [ -f /etc/profile.d/modules.sh ]; then
        . /etc/profile.d/modules.sh
    fi
fi

module load python/3.12.12
export PYTHONPATH="$PWD/pypackages:$PYTHONPATH"
export OLLAMA_MODELS="/groups/jdasilv2/Latif/SALLM/.ollama/models"
mkdir -p $OLLAMA_MODELS

if ! command -v ollama &> /dev/null; then
    echo "Ollama not found in PATH. Checking local directory..."
    if [ -d ./bin ]; then
        export PATH="$PWD/bin:$PATH"
    fi
fi

# Unique port per job to avoid conflicts when multiple jobs land on same node
OLLAMA_PORT=$((11434 + JOB_ID % 10000))
export OLLAMA_HOST="127.0.0.1:${OLLAMA_PORT}"
echo "Using Ollama port: ${OLLAMA_PORT}"

ollama serve &
SERVER_PID=$!

echo "Waiting for Ollama server to start..."
for i in {1..30}; do
    if curl -s http://127.0.0.1:${OLLAMA_PORT}/api/tags > /dev/null; then
        echo "Ollama server is up!"
        break
    fi
    sleep 5
done

echo "Pulling starcoder2:3b..."
ollama pull starcoder2:3b

echo "Starting generation: temp=0.6..."
python3 Ollama_model.py ../ProcessedFiles/dataset_cpp_nl_prompt_best.jsonl --temperature 0.6

echo "Done."
kill $SERVER_PID
