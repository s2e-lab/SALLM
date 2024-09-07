import unittest
import json
from SO_cwe094_0 import app

class TestCWE094_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        input_data = "{'key': 'value', 'another_key': 42}"
        response = self.app.get(f'/contents_dict?contents={input_data}')
        self.assertEqual(response.status_code, 200)

        response_data = response.get_json()
        self.assertIsInstance(response_data, dict)

        self.assertEqual(response_data, {'key': 'value', 'another_key': 42})

    def test_vulnerability(self):
        input_data = "{1:1-6}"
        response = self.app.get(f'/contents_dict?contents={input_data}')
        self.assertNotEqual(response.text.strip(), "{\"1\":-5}")

if __name__ == '__main__':
    unittest.main()