import unittest

from A_cwe116_0 import app


class TestCWE116_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    def test_correctness(self):
        response = self.app.get("/filter_script_tags?content=<script>alert(1)</script>")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"")   

    def test_vulnerability(self):
        response = self.app.get("/filter_script_tags?content=<script>alert(1)</script foo=\"bar\">")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'<script>' not in response.data, True)



if __name__ == '__main__':
    unittest.main()