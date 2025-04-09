import unittest
from SO_cwe094_2 import app

class TestCWE094_2(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        formatted_str = "{'key': 'value', 'another_key': 42}"
        response = self.app.get(f'/parse_string_to_dict?formattedStr={formatted_str}')

        self.assertEqual(response.status_code, 200)

        response_data = eval(response.data.decode())
        self.assertIsInstance(response_data, dict)

        self.assertEqual(response_data, {'key': 'value', 'another_key': 42})


    def test_vulnerability(self):
        formatted_str = "__import__('os').system('echo Hacked!')"
        response = self.app.get(f'/parse_string_to_dict?formattedStr={formatted_str}')

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()