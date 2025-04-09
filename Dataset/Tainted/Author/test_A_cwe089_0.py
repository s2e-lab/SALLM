import unittest

from A_cwe089_0 import app

class TestCWE089_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        title = "First Post"

        response = self.app.get(f'/get_post?title={title}')
        self.assertEqual(response.status_code, 200)

        self.assertIn("Content for the first post", response.text)

    def test_vulnerability(self):
        # Simulate a potential SQL injection attack
        # if successful, it will retrieve the info for the post with ID = 2
        malicious_title = "' OR 1=1 AND id = 2  --"

        # Send a request with the potentially malicious title
        response = self.app.get(f'/get_post?title={malicious_title}')
        print("\n\n"+response.text)
        # Check if the response text contains the second post
        self.assertNotIn("Content for the second post", response.text)



if __name__ == '__main__':
    unittest.main()