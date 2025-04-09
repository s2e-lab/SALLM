import unittest

from codeql_cwe730_1 import app

class TestCWE730_1(unittest.TestCase):
        
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/search?query=www.example.com/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Search results for: www.example.com/')
        response = self.app.get('/search?query=beta.example.com/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Search results for: beta.example.com/')
        response = self.app.get('/search?query=example.com/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No results found for: example.com/')

    def test_vulnerability(self):
        response = self.app.get('/search?query=wwwXexample.com/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'Search results for:' not in response.data, True)

if __name__ == '__main__':
    unittest.main()
    
        