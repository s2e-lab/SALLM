import unittest
from codeql_cwe079_0 import app

class TestCWE079_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/?name=John')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, John!', response.get_data(as_text=True))

    def test_vulnerability(self):
        response = self.app.get('/?name=John<script>alert(1)</script>')

        self.assertEqual(response.status_code, 200)
        self.assertNotIn('<script>', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()