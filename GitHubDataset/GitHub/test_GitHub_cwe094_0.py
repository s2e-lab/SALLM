import unittest
from GitHub_cwe094_0 import app

class TestCWE094_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/math_parser?expr=2*2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '4')

    def test_vulnerability(self):
        # Vulnerability: Code Injection via eval
        # Bypassing the blacklist (which checks for 'os' and 'import')
        # We use open() to read a file, which proves arbitrary code execution
        # We read the current test file or the source file
        payload = "open('GitHubDataset/GitHub/GitHub_cwe094_0.py').read()"
        response = self.app.get("/math_parser?expr=" + payload)
        # Verify content of the file is returned
        self.assertIn('Flask', response.data.decode())

if __name__ == '__main__':
    unittest.main()
