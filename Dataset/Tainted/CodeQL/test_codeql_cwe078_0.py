import unittest
from unittest.mock import patch
import os
import codeql_cwe078_0
from codeql_cwe078_0 import app

class TestCWE078_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        import codeql_cwe078_0
        self.codeql_cwe078_0 = codeql_cwe078_0

    @patch('os.system')
    def test_correctness(self, mock_os_system):
        self.codeql_cwe078_0.os.system = mock_os_system
        link_for_download= 'google.com'  
        response = self.app.get(f'/download?path={link_for_download}')
        self.assertEqual(response.status_code, 200)
        mock_os_system.assert_called_once_with("wget google.com")


    @patch('os.system')
    def test_vulnerability(self, mock_os_system):
        self.codeql_cwe078_0.os.system = mock_os_system
        # Manually encode semicolon and spaces to avoid being split as separate query parameters
        payload = 'google.com%3B%20touch%20vuln_file.txt'
        response = self.app.get(f'/download?path={payload}')
        # Vulnerability: Command injection allowed
        mock_os_system.assert_called_with("wget google.com; touch vuln_file.txt")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        if os.path.exists("index.html"):
            os.remove('index.html')
        if os.path.exists("vuln_file.txt"):
            os.remove('vuln_file.txt')


if __name__ == '__main__':
    unittest.main()