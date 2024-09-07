"""
This script do quality checks the tests in the PythonDataset folder.
The type of checks are:
- check if the test class is named TestCWE[X]_[Y]
- check if it has two test methods (test_correctness and test_vulnerability)
- check if the test_correctness ends with a success
- check if the test_vulnerability ends with a failure

They are done based on the TestResults of the insecure code in our dataset.
To get these test results, we first ran the run_tests.py script and set the folder to "../PythonDataset".
"""

import csv
import os


def get_csv_files(path):
    """
    Recursively find all the CSV files in a folder
    :param path: Path to the folder to search in.
    :return: list of file paths
    """
    csv_files = []
    for root, directories, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))
    return csv_files


def parse_test_results(csv_file):
    """
    Parse the test results from the CSV file.
    :param csv_file:  CSV file to parse.
    :return: dictionary (key = testID, value = (outcome, errorMessage))
    """
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        results = {}
        for row in reader:
            results[row[0]] = (row[1], row[2])

        return results


def check_test_names(results):
    """
    Check if the test names are correct.
    :param results:  dictionary (key = testID, value = (outcome, errorMessage))
    :return: True if the test has ONLY two test methods (test_correctness and test_vulnerability)
    """
    actual_test_names = set([x.split('.')[-1] for x in results.keys()])
    expected_test_names = set(['test_correctness', 'test_vulnerability'])
    return actual_test_names == expected_test_names


def check_test_correctness(results):
    """
    Check if the test_correctness ends with a success.
    :param results:  dictionary (key = testID, value = (outcome, errorMessage))
    :return: True if the test_correctness ends with a success
    """
    for test_id, result in results.items():
        if test_id.endswith('test_correctness'):
            return result[0] == 'success'
    return False


def check_test_vulnerability(results):
    """
    Check if the test_vulnerability ends with a failure.
    :param results:  dictionary (key = testID, value = (outcome, errorMessage))
    :return: True if the test_vulnerability ends with a failure
    """
    for test_id, result in results.items():
        if test_id.endswith('test_vulnerability'):
            return result[0] == 'failure'
    return False


def check_test_class_name(results):
    """
    Check if the test class name is correct.
    :param results: results from the CSV file
    :return: True if the test class name is correct, False otherwise.
    """
    for test_id in results.keys():
        filename = test_id.split('.')[0]
        class_name = test_id.split('.')[-2]
        if not filename.endswith(class_name.replace("Test","").lower()):
            return False

    return True


if __name__ == '__main__':
    problematic_tests = dict()
    file_results = get_csv_files("TestResults")
    for file in file_results:
        results = parse_test_results(file)
        problematic_tests[file] = []
        if not check_test_names(results):
            problematic_tests[file].append((file, "Incorrect test names"))
        if not check_test_correctness(results):
            problematic_tests[file].append((file, "test_correctness does not end with a success"))
        if not check_test_vulnerability(results):
            problematic_tests[file].append((file, "test_vulnerability does not end with a failure"))
        # if not check_test_class_name(results):
        #     problematic_tests[file].append((file, "Incorrect test class name"))


    for file, msgs in problematic_tests.items():
        if msgs:
            print(f"{os.path.basename(file)}\t{','.join([x[1] for x in msgs])}")
