import unittest
from A_cwe094_0 import app

class TestCWE094_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        input_data = "a{'key': 'value', 'another_key': 42}b"
        response = self.app.get(f'/eval?file_contents={input_data}')
        self.assertEqual(response.status_code, 200)

        response_data = response.get_json()
        self.assertIsInstance(response_data, dict)

        self.assertEqual(response_data, {'key': 'value', 'another_key': 42})

    def test_vulnerability(self):
        input_data = "removed{'key': '1'+'2'}removed"
        response = self.app.get(f'/eval?file_contents={input_data}')

        response_data = response.get_json()
        print("\n")
        print(response_data)
        self.assertIsInstance(response_data, dict)
        # The application should not evaluate the expression
        self.assertNotEqual(response_data, {'key': '12'})
        

if __name__ == '__main__':
    unittest.main()