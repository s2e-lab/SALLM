#!/bin/bash
#$ -S /bin/bash
#$ -pe smp 16
#$ -q gpu
#$ -l gpu=2
#$ -N gen_cpp_ollama_github
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
# Ensure Ollama binary is available
if ! command -v ollama &> /dev/null; then
    echo "Ollama not found in PATH. Checking local directory..."
    if [ ! -f ./bin/ollama ]; then
        echo "Ollama binary not found in ./bin. Checking for archive..."
        if [ ! -f ./ollama.tar.zst ]; then
            echo "Archive not found. Downloading..."
            curl -L https://github.com/ollama/ollama/releases/download/v0.17.7/ollama-linux-amd64.tar.zst -o ollama.tar.zst
        fi
        echo "Extracting Ollama..."
        tar --zstd -xf ollama.tar.zst
    fi
    # Add extracted bin to PATH if it exists
    if [ -d ./bin ]; then
        export PATH="$PWD/bin:$PATH"
    fi
fi

# Start Ollama
echo "Starting Ollama server..."
ollama serve &
SERVER_PID=$!
sleep 30

# Pull model
echo "Pulling model starcoder2:3b..."
ollama pull starcoder2:3b

# Run Generations
echo "Starting Ollama Generations (Starcoder2:3b) — GitHub dataset..."
python3 Ollama_model.py ../ProcessedFiles/github-dataset_cpp_nl_prompt_best.jsonl

kill $SERVER_PID
echo "Ollama Generation complete."
