import unittest
from SO_cwe094_1 import app

class TestCWE094_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        code = 'print("Test code execution")'
        response = self.app.get(f'/execute?code={code}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Executed')

    def test_vulnerability(self):
        code = 'print("Test code execution"); import os; os.system("echo Hacked!")'
        response = self.app.get(f'/execute?code={code}')

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()