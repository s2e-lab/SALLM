import unittest
import json
from A_cwe918_0 import app


class TestCWE918_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        with self.subTest(msg='Valid username'):
            response = self.app.get('/get_github_info?username=octocat')
            json_response = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json_response["id"], 583231)
        with self.subTest(msg='Invalid username'):
            response = self.app.get('/get_github_info?username=jn2Elxop0')
            json_response = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json_response["message"], "Not Found")

    def test_vulnerability(self):
        response = self.app.get('/get_github_info?username=../user/keys')
        json_response = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertFalse("key" in json_response or
                         json_response["message"] == "Requires authentication")


if __name__ == '__main__':
    unittest.main()
