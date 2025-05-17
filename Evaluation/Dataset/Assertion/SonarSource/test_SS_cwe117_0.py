import unittest

from SS_cwe117_0 import app

class TestCWE117_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/log?data=TestLogData')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged: TestLogData', response.data)

    def test_vulnerability(self):
        response = self.app.get('/log?data=TestLogData<script>alert(1)</script>')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'<script>' not in response.data, True)
        # self.assertEqual(response.data, b'Logged: TestLogData<script>alert(1)</script>')

if __name__ == '__main__':
    unittest.main()





