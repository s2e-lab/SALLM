"""
Utility script to create a template Dockerfile and requirements.txt for all prompts.

Usage:
    python create_docker_images.py
"""

import os


def get_files(path):
    """
    Recursively find all Python file prompts in the specified path.

    :param path: Path to the folder to search in.
    """
    python_files = []

    for root, directories, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                if '_cwe' in file and 'test_' not in file:
                    python_files.append(os.path.join(root, file))

    return python_files


def create_image(python_file, test_runner_contents):
    """
    Create a Dockerfile and requirements.txt for the specified Python file.
    :param python_file: python file with the prompt
    :param test_runner_contents: contents of the test_runner_template.py file to be written into the dockerfile.
    :return:
    """
    # get filename and parent directory
    filename = os.path.basename(python_file)
    parent_dir = os.path.dirname(python_file)

    # create a dockerfile named filename_Dockerfile
    dockerfile = filename.split('.')[0] + '_Dockerfile'
    # create a requirements.txt named filename_requirements.txt
    requirements = filename.split('.')[0] + '_requirements.txt'

    # create a dockerfile
    with open(os.path.join(parent_dir, dockerfile), 'w') as f:
        f.write(f"FROM python:3.10-slim\n\n")
        f.write(f"WORKDIR /prompt\n\n")
        f.write(f"COPY $SCRIPT_PATH .\n\n")
        f.write(f"COPY test_{filename} .\n\n")
        f.write(f"COPY {requirements} .\n\n")
        f.write(f"RUN pip install --no-cache-dir -r {requirements}\n\n")
        f.write(f"RUN echo \"{test_runner_contents}\" > test_runner.py\n\n")
        f.write(f"CMD [\"python\", \"test_runner.py\", \"test_{filename.split('.')[0]}\"]\n")

    # create a requirements.txt file with Flask installed
    with open(os.path.join(parent_dir, requirements), 'w') as f:
        f.write(f"Flask==2.3.3\n")
        f.write(f"Flask-SQLAlchemy==3.0.5\n")
        f.write(f"pycryptodome==3.19.0\n")

    print(f"Created Dockerfile and requirements.txt for {python_file}.")


def read_test_runner(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()
    # escape the double quotes in the contents and new line characters
    return contents.replace("\"", "\\\"").replace("\n", "\\n")


def fix_dockerfiles(python_files):
    """
    This function is used to make quick fixes to the docker file images.
    Right now it is simply adding a line to declare the argument SCRIPT_PATH
    :param python_files: a list of python files with the canonical solution
    :return:
    """
    for python_file in python_files:
        filename = os.path.basename(python_file)
        parent_dir = os.path.dirname(python_file)
        dockerfile = filename.split('.')[0] + '_Dockerfile'
        with open(os.path.join(parent_dir, dockerfile), 'r') as f:
            contents = f.read()

        # add the declaration of the SCRIPT_PATH variable
        new_content = contents.replace("COPY $SCRIPT_PATH .","ARG SCRIPT_PATH\nCOPY $SCRIPT_PATH .")
        if new_content != contents:
            with open(os.path.join(parent_dir, dockerfile), 'w') as f:
                f.write(new_content)
            print("Fixed the dockerfile for", python_file)




if __name__ == "__main__":
    python_files = get_files("../PythonDataset")
    fix_dockerfiles(python_files)
    # test_runner_contents = read_test_runner("test_runner_template.py")
    # for prompt_file in python_files:
    #     create_image(prompt_file, test_runner_contents)
