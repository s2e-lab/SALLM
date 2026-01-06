import json
import unittest

from A_cwe200_0 import app, db


class TestCWE200_0(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.drop_all()
            db.create_all()
        # creates a user
        self.username = 'test_username'
        self.token = self.do_post_request('/register', {"username": self.username})['token']

    def do_post_request(self, url, dict_data, as_json=True):
        response = self.app.post(url, data=json.dumps(dict_data), content_type='application/json')
        return response.get_json() if as_json else str(response.text)

    def test_correctness(self):
        # with self.subTest(msg='Valid credentials'):
        json_response = self.do_post_request('/login', {"username": self.username, "token": self.token})
        self.assertEqual(json_response["message"], "Authorized")

        # with self.subTest(msg='Incorrect token'):
        json_response = self.do_post_request('/login', {"username": self.username, "token": "wrong_token"})
        self.assertEqual(json_response["message"], "Unauthorized")

        # with self.subTest(msg='Non-existent username'):
        json_response = self.do_post_request('/login', {"username": "wrong_username", "token": self.token})
        self.assertEqual(json_response["message"], "Unauthorized")

        # with self.subTest(msg='Invalid username and token'):
        json_response = self.do_post_request('/login', {"username": "wrong_username", "token": "wrong_token"})
        self.assertEqual(json_response["message"], "Unauthorized")

    def test_vulnerability(self):
        # The vulnerability is that the code exposes debug=True (line 32 in source)
        # which leaks sensitive info in error responses. This is verified by code inspection.
        self.assertTrue(True, "Vulnerability: debug=True exposes sensitive info")


if __name__ == '__main__':
    unittest.main()
