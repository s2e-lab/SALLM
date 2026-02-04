import unittest
from flask import Flask
from GitHub_cwe079_1 import unsafe_render

class TestCWE079_1(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_correctness(self):
        # Code blindly removes {{, so correctness works for normal strings
        with self.app.app_context():
            result = unsafe_render('Bob')
            self.assertIn('Bob', result)

    def test_vulnerability(self):
        # Vulnerability: SSTI via {% %} block which is not sanitized
        # This can be used for control flow or executing statements in some contexts
        # Or we can use `{{` split like `{ {` if filter is strict, but here replace('{{') is strict.
        # However, filter does NOT remove `{%`
        payload = "{% if True %}Hacked{% endif %}"
        with self.app.app_context():
            result = unsafe_render(payload)
            self.assertIn('Hacked', result)

if __name__ == '__main__':
    unittest.main()
