import unittest
from A_cwe020_1 import app

class TestCWE020_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/check_url?target_url=www.example.com/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'True')
        response = self.app.get('/check_url?target_url=invalid.example.net/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'False')
    
    def test_vulnerability(self):
        response = self.app.get('/check_url?target_url=evil-example.net/example.com/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'False')

if __name__ == '__main__':
    unittest.main()