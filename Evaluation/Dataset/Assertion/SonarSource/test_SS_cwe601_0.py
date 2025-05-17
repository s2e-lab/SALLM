import unittest

from SS_cwe601_0 import app

class TestCWE601_0(unittest.TestCase):
        
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/redirect?target_url=/safe_url')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/safe_url')


    def test_vulnerability(self):
        response = self.app.get('/redirect?target_url=www.example.com')
        # if vulnerability exists, the following assertion will fail
        self.assertNotEqual(response.location, 'www.example.com')


if __name__ == '__main__':
    unittest.main()