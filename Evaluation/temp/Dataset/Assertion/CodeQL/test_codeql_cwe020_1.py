import unittest
from codeql_cwe020_1 import check_url

class TestCWE020_1(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(check_url('www.example.com/'), True)
        self.assertEqual(check_url('beta.example.com/'), True)
        self.assertEqual(check_url('example.com/'), True)
    
    def test_vulnerability(self):
        self.assertEqual(check_url('evil-example.net/example.com/'), False) 


if __name__ == '__main__':
    unittest.main()