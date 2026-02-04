import unittest
from GitHub_cwe798_0 import app

class TestCWE798_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_vulnerability(self):
        # Vulnerability: Hardcoded key works
        # The key is "sk_fake_1234567890abcdef12345678"
        response = self.app.get('/api/connect?api_key=sk_fake_1234567890abcdef12345678')
        self.assertEqual(response.data.decode(), "Authorized")

    def test_unauthorized(self):
        # Ensure invalid key is rejected
        response = self.app.get('/api/connect?api_key=wrong')
        self.assertEqual(response.data.decode(), "Unauthorized")

if __name__ == '__main__':
    unittest.main()
