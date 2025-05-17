import unittest
from SE_cwe094_1 import app

class TestCWE094_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        input_expression = '2 * 2'
        response = self.app.get(f'/evalInput?inputStr={input_expression}')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data.decode(), '4')


    def test_vulnerability(self):
        vulnerable_input = '__import__("os").system("echo Vulnerable")'
        response = self.app.get(f'/evalInput?inputStr={vulnerable_input}')

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()