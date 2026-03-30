#!/bin/bash
#$ -S /bin/bash
#$ -M msiddiq3@nd.edu   # Email address for job notification
#$ -m abe            # Send mail when job begins, ends and aborts
#$ -pe smp 4    # Specify parallel environment and legal core size
#$ -q gpu        # Specify queue
#$ -l gpu=2        # Ollama only needs 1 GPU for 3B model
#$ -N ollama_starcoder_github_dataset_cpp
#$ -cwd
#$ -V
#$ -l h_rt=72:00:00

# Fix for module command on some compute nodes
if ! command -v module &> /dev/null; then
    if [ -f /etc/profile.d/modules.sh ]; then
        . /etc/profile.d/modules.sh
    fi
fi

module load python/3.12.12
export PYTHONPATH="$PWD/pypackages:$PYTHONPATH"

# Setup Ollama Environment
export OLLAMA_MODELS="/groups/jdasilv2/Latif/SALLM/.ollama/models"
mkdir -p $OLLAMA_MODELS

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

# Start Ollama server
export OLLAMA_HOST="127.0.0.1:11434"

# Start server in background
ollama serve &
SERVER_PID=$!

# Wait for server to start
echo "Waiting for Ollama server to start..."
for i in {1..30}; do
    if curl -s http://127.0.0.1:11434/api/tags > /dev/null; then
        echo "Ollama server is up!"
        break
    fi
    echo "Still waiting..."
    sleep 5
done

# Pull model
echo "Pulling starcoder2:3b..."
ollama pull starcoder2:3b

# Run generation
echo "Starting generation script..."
python3 Ollama_model.py ../ProcessedFiles/github-dataset_cpp_nl_prompt_best.jsonl

# Cleanup
echo "Cleaning up..."
kill $SERVER_PID
