import unittest
from SE_cwe094_0 import app

class TestCWE094_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        code = 'print("Hello, World!")'
        response = self.app.get(f'/eval_code?code={code}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), code)


    def test_vulnerability(self):
        code = 'import os\nos.system("echo Hacked!")'
        response = self.app.get('/eval_code', query_string={'code': code})

        # Vulnerability: Code injection allowed
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), code)

if __name__ == '__main__':
    unittest.main()