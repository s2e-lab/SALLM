import os

# Get base directory (Evaluation folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

# where the python dataset is
PYTHON_DATASET_PATH = os.path.join(ROOT_DIR, "Dataset")

# where the github-python dataset is
GITHUB_PYTHON_DATASET_PATH = os.path.join(ROOT_DIR, "GitHubDataset")

# where the github-java dataset is
GITHUB_JAVA_DATASET_PATH = os.path.join(ROOT_DIR, "GitHubDatasetJava")

# where the filtered JSON output metadata was saved
GENERATED_CODE_PATH = os.path.join(ROOT_DIR, "Generation", "Filtered_Output")

# where to save the results for running the tests for the canonical insecure solution from the dataset
TEST_RESULTS = os.path.join(BASE_DIR, "TestResults")

# where the java dataset is
JAVA_DATASET_PATH = os.path.join(ROOT_DIR, "DatasetJava")

# Test folder for intermediate test files
TEST_FOLDER = os.path.join(BASE_DIR, "test")

# Directory where pre-built Apptainer/Singularity .sif images are stored (for run_tests_singularity.py)
SIF_DIR = os.path.join(BASE_DIR, "sif_images")
