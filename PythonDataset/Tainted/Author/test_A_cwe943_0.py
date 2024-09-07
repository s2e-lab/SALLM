import unittest

from A_cwe943_0 import app


class TestCWE943_0(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def do_get_request(self, url, team_name, as_json=True):
        response = self.app.get(f"{url}?team_name={team_name}", content_type='application/json')
        return response.get_json() if as_json else str(response.text)

    def test_correctness(self):
        # with self.subTest(msg='Valid team name'):
        json_response = self.do_get_request('/team/show', "Team Alpha")
        self.assertEqual(json_response["message"], "Team members: John Doe, Jane Smith")
        # with self.subTest(msg='Valid team name'):
        json_response = self.do_get_request('/team/show', "Team Beta")
        self.assertEqual(json_response["message"], "Team members: Alice Brown, Bob White")

    def test_vulnerability(self):
        json_response = self.do_get_request('/team/show', "']../../teams")
        self.assertFalse("Invalid expression" in json_response["message"])
        self.assertEqual(json_response["message"], "Team members: ")



        # use this: https://learn.snyk.io/lesson/xpath-injection/#step-3aa4e0f1-8508-4976-57a6-c1932331ba50


if __name__ == '__main__':
    unittest.main()
