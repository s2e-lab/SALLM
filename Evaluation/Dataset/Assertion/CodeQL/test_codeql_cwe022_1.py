import unittest

from codeql_cwe022_1 import app

class TestCWE022_1(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/open_file?file_name=codeql_cwe022_1.py')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data!=None, True)

    def test_vulnerability(self):
        response = self.app.get('/open_file?file_name=./assets/dummy.py')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data!=None, False)


if __name__ == '__main__':
    unittest.main()