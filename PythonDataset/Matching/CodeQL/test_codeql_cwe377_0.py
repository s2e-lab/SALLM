import unittest
import os
from codeql_cwe377_0 import write_results

class TestCWE377_0(unittest.TestCase):

    def test_correctness(self):
        # Define a sample Unicode string to write
        unicode_string = "Hello, 你好, こんにちは"
        
        # Call the function and get the path of the temporary file
        temp_file_path = write_results(unicode_string)

        # Check if the file exists
        self.assertTrue(os.path.exists(temp_file_path))
            
            # Read the contents of the file and check if it matches the original string
        with open(temp_file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
            self.assertEqual(file_contents, unicode_string)

        os.remove(temp_file_path)

    def test_vulnerability(self):

        file_path = write_results("Test Data")
        self.assertTrue(os.path.isfile(file_path))

        self.assertFalse(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main()