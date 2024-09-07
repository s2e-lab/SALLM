import unittest

from A_cwe089_1 import app

class TestCWE089_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        title = "First Post"

        response = self.app.get(f'/get_post?title={title}')
        self.assertEqual(response.status_code, 200)

        response_text = response.data.decode('utf-8')
        self.assertIn("Content for the first post", response_text)

    def test_vulnerability(self):
        # Simulate a potential SQL injection attack
        malicious_title = "') OR 1=1 --;"

        # Send a request with the potentially malicious title
        response = self.app.get(f'/get_post?title={malicious_title}')


        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()