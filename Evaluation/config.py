import os

# where the python dataset is
PYTHON_DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Dataset")

# a temporary folder where the generated code will be copied to
TEMP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")

# where the filtered JSON output metadata was saved
GENERATED_CODE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Filtered_Output")

# where the results for running the tests are
TEST_MODEL_RESULTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TestModelsResults")

# where to save the results for running the tests for the canonical insecure solution from the dataset
TEST_RESULTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TestResults")
