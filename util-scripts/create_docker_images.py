import os
import sys

# Get absolute path to the script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Get absolute path to the project root
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

def get_files(path):
    """
    Recursively find all Python file prompts in the specified path.
    """
    python_files = []
    if not os.path.isabs(path):
        path = os.path.abspath(os.path.join(SCRIPT_DIR, path))

    for root, directories, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                # Identifying prompts by _cwe and absence of test_ prefix
                if '_cwe' in file and not file.startswith('test_'):
                    python_files.append(os.path.join(root, file))

    return python_files

def create_image(python_file, test_runner_contents):
    """
    Create a Dockerfile and requirements.txt for the specified Python file.
    """
    filename = os.path.basename(python_file)
    parent_dir = os.path.dirname(python_file)
    name_no_ext = os.path.splitext(filename)[0]

    dockerfile_name = f"{name_no_ext}_Dockerfile"
    requirements_name = f"{name_no_ext}_requirements.txt"
    dockerfile_path = os.path.join(parent_dir, dockerfile_name)
    requirements_path = os.path.join(parent_dir, requirements_name)

    # Standard requirements for the dataset
    standard_reqs = [
        "Flask==2.3.3",
        "Flask-SQLAlchemy==3.0.5",
        "pycryptodome==3.19.0",
        "requests==2.31.0",
        "cryptography==41.0.3"
    ]

    # Write requirements.txt
    with open(requirements_path, 'w') as f:
        for req in standard_reqs:
            f.write(f"{req}\n")

    # Write test_runner.py locally in the same directory for Docker context
    test_runner_path = os.path.join(parent_dir, "test_runner.py")
    with open(test_runner_path, 'w') as f:
        f.write(test_runner_contents)

    # Create Dockerfile
    docker_content = [
        "FROM python:3.10-slim",
        "",
        "WORKDIR /prompt",
        "",
        f"COPY {filename} .",
        f"COPY test_{filename} .",
        f"COPY {requirements_name} requirements.txt",
        "COPY test_runner.py .",
        "",
        "RUN pip install --no-cache-dir -r requirements.txt",
        "",
        "# Option to inject solution at build time",
        "ARG SCRIPT_CONTENT",
        f"RUN if [ ! -z \"$SCRIPT_CONTENT\" ]; then echo \"$SCRIPT_CONTENT\" | base64 -d > {filename}; fi",
        "",
        f"CMD [\"python\", \"test_runner.py\", \"test_{name_no_ext}\"]"
    ]

    with open(dockerfile_path, 'w') as f:
        f.write("\n".join(docker_content) + "\n")

    print(f"Created Docker resources for {python_file}.")

def read_test_runner(file_path):
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(os.path.join(SCRIPT_DIR, file_path))
    with open(file_path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    # Target the Dataset directory relative to the script
    dataset_path = os.path.join(PROJECT_ROOT, "Dataset")
    python_files = get_files(dataset_path)
    
    # Read the test runner template once
    template_path = os.path.join(SCRIPT_DIR, "test_runner_template.py")
    test_runner_contents = read_test_runner(template_path)
    
    for prompt_file in python_files:
        create_image(prompt_file, test_runner_contents)
