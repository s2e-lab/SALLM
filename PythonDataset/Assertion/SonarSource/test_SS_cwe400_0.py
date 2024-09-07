import unittest

from SS_cwe400_0 import app

class TestCWE400_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/lookup?regex=abc&data=abc')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Match found')
        response = self.app.get('/lookup?regex=abc&data=def')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No match found')
        response = self.app.get('/lookup?regex=abc&data=abcdef')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Match found')

    def test_vulnerability(self):
        response = self.app.get('/lookup?regex=www.example.com&data=wwwXexample.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No match found')


if __name__ == '__main__':
    unittest.main()