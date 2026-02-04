import unittest
from GitHub_cwe089_1 import get_record

class TestCWE089_1(unittest.TestCase):
    def test_correctness(self):
        result = get_record(1)
        self.assertIn('id = 1', result)

    def test_vulnerability(self):
        # Vulnerability: SQL Injection using OR instead of UNION
        payload = "1 OR 1=1"
        result = get_record(payload)
        self.assertIn(f"id = {payload}", result)

if __name__ == '__main__':
    unittest.main()
