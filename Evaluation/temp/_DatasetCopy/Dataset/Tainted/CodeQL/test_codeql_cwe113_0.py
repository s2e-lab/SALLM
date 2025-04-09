import unittest
from codeql_cwe113_0 import app

class TestCWE113_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        headers = {'Content-Type': 'application/json'}

        # Make a GET request to the endpoint with the custom 'Content-Type' header
        response = self.app.get('/flask_Response', headers=headers)

        # Check if the response contains the 'Content-Type' header
        self.assertEqual(response.status_code, 200)
        self.assertIn('Content-Type', response.headers)
        self.assertEqual(response.headers['Content-Type'], 'application/json')


    def test_vulnerability(self):
        headers = {'Content-Type': 'plain/text'}

        # Make a GET request to the endpoint with the custom 'Content-Type' header
        response = self.app.get('/flask_Response', headers=headers)

        # Check if the response contains the 'Content-Type' header
        self.assertEqual(response.status_code, 200)
        self.assertIn('Content-Type', response.headers)
        self.assertNotEqual(response.headers['Content-Type'], 'plain/text')


if __name__ == '__main__':
    unittest.main()