import os

# Get base directory (Evaluation folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

# where the python dataset is
PYTHON_DATASET_PATH = os.path.join(ROOT_DIR, "Dataset")

# a temporary folder where the generated code will be copied to
TEMP_PATH = os.path.join(BASE_DIR, "temp")

# where the filtered JSON output metadata was saved
GENERATED_CODE_PATH = os.path.join(ROOT_DIR, "Generation", "Filtered_Output")

# where the results for running the tests are
TEST_MODEL_RESULTS = os.path.join(BASE_DIR, "TestModelsResults_Python")

# where to save the results for running the tests for the canonical insecure solution from the dataset
TEST_RESULTS = os.path.join(BASE_DIR, "TestResults")

# where the java dataset is
JAVA_DATASET_PATH = os.path.join(ROOT_DIR, "DatasetJava")

# Test folder for intermediate test files
TEST_FOLDER = os.path.join(BASE_DIR, "test")
