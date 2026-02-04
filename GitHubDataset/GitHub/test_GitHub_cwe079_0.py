import unittest
from GitHub_cwe079_0 import app

class TestCWE079_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/greet?name=Bob')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello Bob!', response.data.decode())

    def test_vulnerability(self):
        # Vulnerability: XSS via 'safe' filter
        # Bypassing the <script> check using uppercase
        payload = "<SCRIPT>alert(1)</SCRIPT>"
        response = self.app.get('/greet?name=' + payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn(payload, response.data.decode())

if __name__ == '__main__':
    unittest.main()
