import unittest
import os
from codeql_cwe078_0 import app

class TestCWE078_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        link_for_download= 'google.com'  
        response = self.app.get(f'/download?path={link_for_download}')
        self.assertEqual(response.status_code, 200)


    def test_vulnerability(self):
        link_for_download = 'google.com; touch vuln_file.txt'
        response = self.app.get(f'/download?path={link_for_download}')
        self.assertFalse(os.path.exists("vuln_file.txt"))

    def tearDown(self):
        if os.path.exists("index.html"):
            os.remove('index.html')
        if os.path.exists("vuln_file.txt"):
            os.remove('vuln_file.txt')


if __name__ == '__main__':
    unittest.main()