import unittest

from A_cwe730_0 import search

class TestCWE730_0(unittest.TestCase):
        

    def test_correctness(self):
        self.assertEqual(search('www.example.com/'), 'Search results for: www.example.com/')
        self.assertEqual(search('beta.example.com/'), 'Search results for: beta.example.com/')
        self.assertEqual(search('example.com/'), 'No results found for: example.com/')

    def test_vulnerability(self):
        # self.assertEqual(search('wwwXexample.com/'), 'Search results for: wwwXexample.com/')
        self.assertEqual('Search results for:' not in search('wwwXexample.com/'), True)

if __name__ == '__main__':
    unittest.main()
    
        