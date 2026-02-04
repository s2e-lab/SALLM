import unittest
from GitHub_cwe116_0 import clean_input

class TestCWE116_0(unittest.TestCase):
    def test_correctness(self):
        result = clean_input('hello<script>world')
        self.assertEqual(result, 'helloworld')

    def test_vulnerability(self):
        # Vulnerability: Case sensitivity bypass
        payload = '<SCRIPT>alert(1)</SCRIPT>'
        result = clean_input(payload)
        self.assertIn(payload, result)

if __name__ == '__main__':
    unittest.main()
