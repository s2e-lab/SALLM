import unittest
from SO_cwe094_4 import app

class TestCWE094_4(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        equation = '2 * 2'
        response = self.app.get(f'/parse_math_equation?equation={equation}')

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response data is the result of the evaluated equation
        response_data = response.data.decode()
        self.assertEqual(response_data, '4')

    def test_vulnerability(self):
        equation = "__import__('os').system('echo Hacked!')"
        response = self.app.get(f'/parse_math_equation?equation={equation}')

        # Check that the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()