import unittest
from codeql_cwe176_0 import app

class TestCWE176_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        ui_data = "John"
        response = self.app.get(f'/result?ui_data={ui_data}')

        self.assertEqual(response.status_code, 200)

        self.assertEqual("John", response.data.decode('utf-8'))
            
    def test_vulnerability(self):
        ui_data = "Café"
        response = self.app.get(f'/result?ui_data={ui_data}')

        self.assertEqual(response.status_code, 200)

        self.assertEqual("Café", response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()