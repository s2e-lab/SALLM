"""
This script runs all the tests in the PythonDataset folder as well as the code generated by the models.
@Author: Joanna C S Santos
"""
import concurrent.futures
import json
import os
import shutil
import subprocess
import sys
import time
from config import PYTHON_DATASET_PATH, TEMP_PATH, GENERATED_CODE_PATH, TEST_MODEL_RESULTS, TEST_RESULTS
from tqdm import tqdm

# ================= FLAGS TO CONFIGURE THE ANALYSIS =================
DEBUG = False  # if enabled, it will print the output of the Docker commands to stdout
RUN_SEQUENTIAL = False  # if enabled, it will run the tests sequentially
# if true, it will test the LLM-generated code; otherwise, it runs the tests on the dataset's insecure code
RUN_TESTS_ON_GENERATED_CODE = True
# ========================== END OF FLAGS ===========================


# where to redirect stdout/stderr
STDOUT = sys.stdout if DEBUG else subprocess.DEVNULL
STDERR = subprocess.STDOUT if DEBUG else subprocess.DEVNULL


def get_python_files(path):
    """
    Recursively find all Python file prompts in the specified path.

    :param path: Path to the folder to search in.
    """
    python_files = []

    for root, directories, files in os.walk(path):
        for file in files:
            if file.endswith(".py") and '_cwe' in file and 'test_' not in file:
                python_files.append(os.path.join(root, file))

    return python_files


def get_output(model_name, data):
    """
    Get the output from the specified model.
    It has to parse the JSON output differently depending on the model because each model has a different format.
    :param model_name: name of the LLM
    :param data: current JSON line
    :return: a list of outputs
    """
    if "gpt-4" in model_name or "gpt-3.5" in model_name:
        return data["output"]["choices"]
    return data["output"]


def save_generated_code(jsonl_folder_path, temp_folder_path):
    """
    Get all the filtered outputs (in JSONL files) from the specified path.
    :param jsonl_folder_path: a path to a directory that has all the JSONL files.
    :param temp_folder_path: a path to a directory that will have all the generated code.
    :return:
    """
    # Get list of all files in the directory
    files = os.listdir(jsonl_folder_path)
    jsonl_files = [os.path.join(jsonl_folder_path, file) for file in files if
                   file.endswith('.jsonl')]

    for jsonl_file in jsonl_files:
        with open(jsonl_file, 'r') as f:
            model_id = os.path.basename(jsonl_file).split('.jsonl')[0].split('_')[1:]
            temperature = model_id[-1]
            model_name = '_'.join(model_id[:-1]).replace("Salesforce_", "")
            for d in [json.loads(line) for line in f.readlines()]:
                output_id = d['id']
                technique = d['technique']
                source = d['source']
                file_name = '_'.join(output_id.split('_')[2:])

                output_idx = 0
                for output in get_output(model_name, d):
                    output_idx += 1
                    cleared_code = output["cleared_code"]

                    # create a temporary file to write the cleared code on a temporary folder
                    temp_file = os.path.join(os.getcwd(),
                                             temp_folder_path,
                                             f"{model_name}_{temperature}_{technique}_R{output_idx}",
                                             file_name)
                    temp_folder = os.path.dirname(temp_file)
                    if not os.path.exists(temp_folder): os.makedirs(temp_folder)
                    with open(temp_file, 'w', encoding="utf-8") as f:
                        f.write(cleared_code)


def copy_to_temp(source_dir, temp_dir):
    # Recursively copy the source directory to the temporary directory
    to_path = os.path.join(temp_dir, os.path.basename(source_dir))
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(source_dir, to_path)

    return temp_dir


def get_source(filename):
    """
    Get the source of the generated code.
    :param filename: the filename of the generated code.
    :return: the source of the generated code.
    """
    s = filename.split("_")[0]
    if s == "A":
        return "Author"
    elif s == "codeql":
        return "CodeQL"
    elif s == "SO":
        return "StackOverflow"
    elif s == "SS":
        return "SonarSource"
    elif s == "SE":
        return "SecurityEval"
    elif s == "Mitre":
        return "CWEList"

    raise Exception(f"Unknown source: {s}")


def process_python_file(python_file):
    """
    Run tests on docker container for the specified python file.
    :param python_file:  python file with the prompt.
    """
    filename = os.path.basename(python_file).split('.')[0]
    parent_dir = os.path.dirname(python_file)
    test_file_results = f'test_{filename}_results.csv'

    if os.path.abspath(PYTHON_DATASET_PATH) in os.path.abspath(python_file):
        model, temperature, technique, index = "Insecure", "Code", parent_dir.split(os.sep)[-2], "X"
        output_folder = os.path.join(TEST_RESULTS,f"{technique}_{test_file_results}")
    else:
        model, temperature, technique, index = os.path.split(parent_dir)[1].rsplit("_", 3)
        output_folder = os.path.join(TEST_MODEL_RESULTS, f"{model}_{temperature}_{index}_{technique}_{test_file_results}")




    docker_file = f'{filename}_Dockerfile'
    source = get_source(filename)
    docker_file_dir = os.path.abspath(os.path.join(PYTHON_DATASET_PATH, technique, source))
    docker_image_id = f"{model}_{temperature}_{index}_{technique}_{filename}".lower()
    docker_file = os.path.join(docker_file_dir, docker_file)
    # each command is a tuple: (command, working directory to execute the command)
    commands = [
        # build docker image
        (
            f"docker build -t {docker_image_id} -f {docker_file} {docker_file_dir} --build-arg SCRIPT_PATH={os.path.abspath(python_file)}",
            docker_file_dir
        ),
        # run docker image in a container
        (
            f"docker run --name {docker_image_id} {docker_image_id}",
            os.getcwd()
        ),
        # copy test file results back to local machine
        (
            f"docker cp {docker_image_id}:/prompt/{test_file_results} {output_folder}",
            os.getcwd()
        ),
        # remove docker image and container
        (
            f"docker rm {docker_image_id} && docker rmi {docker_image_id}:latest",
            os.getcwd()
        ),
    ]

    # TODO: remove line below, used for debugging only!
    if 'cwe020' not in filename or temperature != '0.0' or 'gpt-3.5' not in docker_image_id: return


    try:
        # run test file in docker container, by running each command
        print(f"Running {docker_image_id}")
        start = time.time()
        for cmd, working_dir in commands:
            print(f"\t{cmd}")
            subprocess.run(cmd, shell=True, check=True, cwd=working_dir, stdout=STDOUT, stderr=STDERR)
        end = time.time()
        print(f"\tFinished {docker_file} in {end - start} seconds.")
    except Exception as e:
        # print to stderr
        print(f"\tFailed to run {docker_file}: {e}", file=sys.stderr)
        try:
            # remove docker image
            subprocess.run(commands[-1][0], shell=True, check=True, cwd=commands[-1][1], stdout=STDOUT, stderr=STDERR)
        except:
            pass


def  run_tests(code_folder):
    """
    Run all the tests in the specified folder.
    :param code_folder: where the generated code was saved
    """
    python_files = get_python_files(code_folder)
    # python_files = [x for x in python_files if "gpt-3" in x ]
    # python_files = [x for x in python_files if "gpt-3" in x or "codegen" in x]
    # python_files = [x for x in python_files if "gpt-4" in x or "starcoder" in x]#TODO: change this if you want to slice down the array for testing,ex: #
    python_files = [x for x in python_files if "_0.0" in x ]
    # run all python files sequentially (useful for debugging)
    if RUN_SEQUENTIAL:
        for python_file in tqdm(python_files, desc="", unit="file", bar_format='{l_bar}{bar}{r_bar}\n'):
            process_python_file(python_file)
    # run all python files in parallel
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            list(tqdm(executor.map(process_python_file, python_files), disable=True, total=len(python_files),
                      desc="Processing files", unit="file"))


if __name__ == "__main__":
    folder_path = TEMP_PATH if RUN_TESTS_ON_GENERATED_CODE else PYTHON_DATASET_PATH

    # copy the generated code to a temporary folder (if needed)
    if RUN_TESTS_ON_GENERATED_CODE:
        print(f"Saving generated code on {TEMP_PATH}...")
        save_generated_code(GENERATED_CODE_PATH, TEMP_PATH)
        print("Finished saving generated code.")

    # run the tests
    start = time.time()
    run_tests(folder_path)
    end = time.time()
    print(f"Finished running tests in {(end - start) / 60} minutes.")





