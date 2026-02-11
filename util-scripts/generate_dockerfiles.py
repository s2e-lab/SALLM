import os
import shutil
import json
import sys
# Add Evaluation directory to path to import config
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Evaluation'))

from config import GITHUB_PYTHON_DATASET_PATH, GITHUB_JAVA_DATASET_PATH

PYTHON_DOCKERFILE_TEMPLATE = """FROM python:3.10-slim

WORKDIR /prompt

# Copy requirements if they exist (created manually in this script)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test runner and the prompt files
COPY {item_id}.py .
COPY test_{item_id}.py .
COPY test_runner.py .

# Default command to run tests
# The test_runner.py expects the test file name without .py
CMD ["python", "test_runner.py", "test_{item_id}"]
"""

# Context for Java is root of GITHUB_JAVA_DATASET_PATH
JAVA_DOCKERFILE_TEMPLATE = """FROM maven:3.8.6-openjdk-8-slim

WORKDIR /app

# Copy pom.xml
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Create directory structure
RUN mkdir -p src/main/java/com/sallm/GitHub/GitHub src/test/java/com/sallm/GitHub/GitHub

# Copy source and test files (paths relative to root)
COPY src/main/java/com/sallm/GitHub/GitHub/{item_id}.java src/main/java/com/sallm/GitHub/GitHub/
COPY src/test/java/com/sallm/GitHub/GitHub/Test{item_id}.java src/test/java/com/sallm/GitHub/GitHub/

# Default command to run tests
CMD ["mvn", "test"]
"""

def generate_python_dockerfiles():
    github_dir = os.path.join(GITHUB_PYTHON_DATASET_PATH, "GitHub")
    
    # 1. Copy test_runner.py to GitHub dataset
    test_runner_src = os.path.join(os.path.dirname(GITHUB_PYTHON_DATASET_PATH), "Dataset", "Assertion", "Author", "test_runner.py")
    test_runner_dest = os.path.join(github_dir, "test_runner.py")
    if os.path.exists(test_runner_src):
        shutil.copy(test_runner_src, test_runner_dest)
        print(f"Copied test_runner.py to {test_runner_dest}")

    # 2. Create a generic requirements.txt
    requirements_path = os.path.join(github_dir, "requirements.txt")
    with open(requirements_path, "w") as f:
        f.write("unittest-xml-reporting\nflask\nrequests\npyyaml\n")
    print(f"Created {requirements_path}")

    # 3. Generate Dockerfiles for each .py file (that isn't a test_)
    files = [f for f in os.listdir(github_dir) if f.endswith(".py") and not f.startswith("test_") and f != "test_runner.py"]
    for f in files:
        item_id = os.path.splitext(f)[0]
        dockerfile_content = PYTHON_DOCKERFILE_TEMPLATE.format(item_id=item_id)
        dockerfile_path = os.path.join(github_dir, f"{item_id}_Dockerfile")
        with open(dockerfile_path, "w") as df:
            df.write(dockerfile_content)
    print(f"Generated {len(files)} Python Dockerfiles")

def generate_java_dockerfiles():
    github_java_pkg_dir = os.path.join(GITHUB_JAVA_DATASET_PATH, "src", "main", "java", "com", "sallm", "GitHub", "GitHub")
    
    # Generate Dockerfiles for each .java file (that isn't a Test)
    files = [f for f in os.listdir(github_java_pkg_dir) if f.endswith(".java") and not f.startswith("Test") and f != "ClassX.java" and not f.endswith("_Dockerfile")]
    for f in files:
        item_id = os.path.splitext(f)[0]
        dockerfile_content = JAVA_DOCKERFILE_TEMPLATE.format(item_id=item_id)
        dockerfile_path = os.path.join(github_java_pkg_dir, f"{item_id}_Dockerfile")
        with open(dockerfile_path, "w") as df:
            df.write(dockerfile_content)
    print(f"Generated {len(files)} Java Dockerfiles")

if __name__ == "__main__":
    generate_python_dockerfiles()
    generate_java_dockerfiles()
