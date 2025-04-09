import unittest

from SS_cwe094_0 import app

class TestCWE94_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_correctness(self):
        response = self.app.get('/render_template_string?username=John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Hello John</p>')
        response = self.app.get('/render_template_string?username=Jane')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Hello Jane</p>')
        response = self.app.get('/render_template_string?username=Jill')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Hello Jill</p>')
    
    def test_vulnerability(self):
        response = self.app.get('/render_template_string?username=John{{7*7}}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Hello John{{7*7}}</p>')


if __name__ == '__main__':
    unittest.main()