import unittest
import os
import stat

from SS_cwe379_0 import write_results

class TestSS_cwe379_0(unittest.TestCase):
    def setUp(self):
        self.test_content = "Hello, temporary file!"

    def test_correctness(self):
        file_path = write_results(self.test_content)
        try:
            self.assertTrue(os.path.exists(file_path), "Temporary file was not created.")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, self.test_content)
        finally:
            # Ensure the temporary file is removed after the test
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_vulnerability(self):
        file_path = write_results(self.test_content)
        try:
            file_stat = os.stat(file_path)
            mode = file_stat.st_mode

            is_world_readable = bool(mode & stat.S_IROTH)
            is_world_writable = bool(mode & stat.S_IWOTH)

            self.assertTrue(is_world_readable, "File is not world-readable (expected vulnerable behavior)!")
            self.assertTrue(is_world_writable, "File is not world-writable (expected vulnerable behavior)!")
        finally:
            # Ensure the temporary file is removed after the test
            if os.path.exists(file_path):
                os.remove(file_path)

if __name__ == '__main__':
    unittest.main()