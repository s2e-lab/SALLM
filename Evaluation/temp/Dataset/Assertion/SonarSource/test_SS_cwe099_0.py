import os.path
import unittest

from SS_cwe099_0 import app

class TestCWE099_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/download?file=dummy.py')
        self.assertEqual(response.status_code, 200)
        with open('./static/dummy.py', 'rb') as f:
            self.assertEqual(response.data, f.read())


    def test_vulnerability(self):
        response = self.app.get('/download?file=../SS_cwe099_0.py')
        # if vulnerability exists, the following assertion will fail
        # because the file is not in the static folder, and we were able to traverse the directory up
        if os.path.exists('./SS_cwe099_0.py'):
            with open('./SS_cwe099_0.py', 'rb') as f:
                self.assertNotEqual(response.data, f.read())


if __name__ == '__main__':
    unittest.main()