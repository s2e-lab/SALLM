import csv
import sys
import unittest


class CSVTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append((test.id(), 'success', ""))

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append((test.id(), 'error', str(err[1])))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append((test.id(), 'failure', str(err[1])))

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['TestName', 'Result', 'Message'])
            writer.writerows(self.results)


def run_and_save(test_suite, filename):
    runner = unittest.TextTestRunner(resultclass=CSVTestResult)
    result = runner.run(test_suite)
    result.save_to_csv(filename)


def is_compilable(script_path):
    """
    Checks whether the script compiles.
    :param script_path: Path to the script file.
    :return: True if compilable, False otherwise.
    """
    try:
        with open(f"{script_path}.py", 'r') as file:
            source_code = file.read()
        # Compile the source code. This will raise a SyntaxError if the code is not compilable.
        compile(source_code, script_path, 'exec')
        return True  # If compile succeeds, the script is compilable.
    except (SyntaxError, TypeError, ValueError):
        # Catch SyntaxError for syntax issues, TypeError or ValueError for other compilation issues.
        return False  # If compile raises an exception, the script is not compilable.


if __name__ == '__main__':
    test_file = sys.argv[1]
    results_csv_file = f'{test_file}_results.csv'
    if is_compilable(test_file):
        test_suite = unittest.defaultTestLoader.loadTestsFromName(test_file)
        run_and_save(test_suite, results_csv_file)
    else:
        with open(results_csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['TestName', 'Result', 'Message'])
            writer.writerows([
                ['test_correctness', 'SyntaxError', 'We could not compile the code'],
                ['test_vulnerability', 'SyntaxError', 'We could not compile the code']
            ])
