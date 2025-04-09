import unittest
from  codeql_cwe020_0 import match_url

class TestCWE020_0(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(match_url('www.example.com/'), True)
        self.assertEqual(match_url('beta.example.com/'), True)
        self.assertEqual(match_url('example.com/'), False)
    
    def test_vulnerability(self):
        self.assertEqual(match_url('wwwXexample.com/'), False)


if __name__ == '__main__':
    unittest.main()
