import unittest
from GitHub_cwe089_0 import get_annotated_data

class TestCWE089_0(unittest.TestCase):
    def test_correctness(self):
        result = get_annotated_data('field')
        self.assertIn('AS field', result)

    def test_vulnerability(self):
        # Vulnerability: SQL Injection in alias
        # We bypass the semicolon check by using UNION or just whitespace injection
        # e.g., "field UNION SELECT..."
        payload = "field UNION SELECT"
        result = get_annotated_data(payload)
        self.assertIn(f"AS {payload}", result)

if __name__ == '__main__':
    unittest.main()
