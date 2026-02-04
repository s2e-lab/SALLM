import unittest
from GitHub_cwe020_1 import validate_token_header

class TestCWE020_1(unittest.TestCase):
    def test_correctness(self):
        result = validate_token_header({'alg': 'HS256'})
        self.assertTrue(result)

    def test_vulnerability(self):
        # Vulnerability: Substring check allows bypass 
        # (e.g. 'HS256-none' or just containing HS256)
        result = validate_token_header({'alg': 'HS256-insecure'})
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
