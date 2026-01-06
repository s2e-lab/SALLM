import os
import sys

# Get absolute path to the script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Get absolute path to the project root
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

def get_java_files(path):
    """
    Recursively find all Java prompt files.
    """
    java_files = []
    if not os.path.isabs(path):
        path = os.path.abspath(os.path.join(SCRIPT_DIR, path))

    for root, directories, files in os.walk(path):
        for file in files:
            if file.endswith(".java"):
                # Identifying prompts by _cwe and absence of Test prefix
                if '_cwe' in file and not file.startswith('Test'):
                    java_files.append(os.path.join(root, file))

    return java_files

def create_java_docker(java_file, pom_contents):
    """
    Create a Dockerfile for the specified Java prompt.
    """
    filename = os.path.basename(java_file)
    parent_dir = os.path.dirname(java_file)
    name_no_ext = os.path.splitext(filename)[0]

    # Find relative path from com/sallm to resolve package structure
    rel_path = os.path.relpath(java_file, os.path.join(PROJECT_ROOT, "DatasetJava", "src", "main", "java"))
    rel_dir = os.path.dirname(rel_path)

    dockerfile_name = f"{name_no_ext}_Dockerfile"
    dockerfile_path = os.path.join(parent_dir, dockerfile_name)

    # Find the corresponding test file
    test_filename = f"Test{filename}"
    test_src_path = os.path.join(PROJECT_ROOT, "DatasetJava", "src", "test", "java", rel_dir, test_filename)
    
    if not os.path.exists(test_src_path):
        print(f"Warning: Test file not found for {java_file} at {test_src_path}")
        return

    # Create Dockerfile
    docker_content = [
        "FROM maven:3.8.6-openjdk-8-slim",
        "",
        "WORKDIR /app",
        "",
        "# Copy pom.xml",
        "COPY pom.xml .",
        "",
        "# Create directory structure",
        f"RUN mkdir -p src/main/java/{rel_dir} src/test/java/{rel_dir}",
        "",
        "# Copy source and test files",
        f"COPY {filename} src/main/java/{rel_dir}/",
        f"COPY Test{filename} src/test/java/{rel_dir}/",
        "",
        "# Option to inject solution at build time",
        "ARG SCRIPT_CONTENT",
        f"RUN if [ ! -z \"$SCRIPT_CONTENT\" ]; then echo \"$SCRIPT_CONTENT\" | base64 -d > src/main/java/{rel_dir}/{filename}; fi",
        "",
        "# Default command to run tests",
        "CMD [\"mvn\", \"test\"]"
    ]

    with open(dockerfile_path, 'w') as f:
        f.write("\n".join(docker_content) + "\n")
    
    # Also write pom.xml and copy the test file to the parent_dir for Docker context if not already there
    # Note: For Docker build, all files must be in the same directory as the Dockerfile.
    pom_path = os.path.join(parent_dir, "pom.xml")
    if not os.path.exists(pom_path):
        with open(pom_path, 'w') as f:
            f.write(pom_contents)

    parent_test_path = os.path.join(parent_dir, test_filename)
    if not os.path.exists(parent_test_path):
        import shutil
        shutil.copy2(test_src_path, parent_test_path)

    print(f"Created Docker resources for {java_file} in {parent_dir}")

if __name__ == "__main__":
    dataset_java_path = os.path.join(PROJECT_ROOT, "DatasetJava", "src", "main", "java", "com", "sallm")
    java_files = get_java_files(dataset_java_path)

    pom_src_path = os.path.join(PROJECT_ROOT, "DatasetJava", "pom.xml")
    with open(pom_src_path, 'r') as f:
        pom_contents = f.read()

    for java_file in java_files:
        create_java_docker(java_file, pom_contents)
