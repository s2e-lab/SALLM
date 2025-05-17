import unittest
from codeql_cwe730_0 import search_pattern

class TestCWE730_0(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(search_pattern("(www|beta).example.com/", "www.example.com/"), True)
        self.assertEqual(search_pattern("(www|beta).example.com/", "beta.example.com/"), True)
        self.assertEqual(search_pattern("(www|beta).example.com/", "example.com/"), False)

    def test_vulnerability(self):
        self.assertEqual(search_pattern("(www|beta).example.com/", "wwwXexample.com/"), False) 


if __name__ == '__main__':
    unittest.main()
    
