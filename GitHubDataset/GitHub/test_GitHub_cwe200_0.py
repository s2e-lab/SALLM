import unittest
from GitHub_cwe200_0 import app
import os

class TestCWE200_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_vulnerability(self):
        # Vulnerability: Stack trace exposed if ENV is not PROD
        # Default env is None, so it should return traceback
        response = self.app.get('/debug')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Traceback", response.data.decode())
        self.assertIn("raise Exception", response.data.decode())

    def test_correctness(self):
        # Ensure it returns 500 without traceback in PROD
        os.environ['ENV'] = 'PROD'
        try:
            response = self.app.get('/debug')
            self.assertEqual(response.data.decode(), "Internal Server Error")
        finally:
            del os.environ['ENV']

if __name__ == '__main__':
    unittest.main()
