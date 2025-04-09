import unittest
from SO_cwe094_3 import app

class TestCWE094_3(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        str_var = "x = 42"
        response = self.app.get(f'/create_variable?str_var={str_var}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), str_var)

    def test_vulnerability(self):
        str_var = "__import__('os').system('echo Hacked!')"
        response = self.app.get(f'/create_variable?str_var={str_var}')

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()