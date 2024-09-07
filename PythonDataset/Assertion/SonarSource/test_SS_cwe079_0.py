import unittest

from SS_cwe079_0 import app

class TestCWE79_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/template_replaced?param=John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<html>\n<body>\nJohn\n</body>\n</html>\n')

    def test_vulnerability(self):
        response = self.app.get('/template_replaced?param=<script>alert(1)</script>')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'<script>' not in response.data, True)


if __name__ == '__main__':
    unittest.main()