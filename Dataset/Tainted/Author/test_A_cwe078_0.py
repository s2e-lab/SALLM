import unittest
from A_cwe078_0 import app
from unittest.mock import patch

class TestCWE078_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('os.system')
    def test_correctness(self, mock_os_system):
        link_to_ping = 'google.com'  
        response = self.app.get(f'/ping?link={link_to_ping}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), link_to_ping)
        mock_os_system.assert_called_with('ping ' + link_to_ping)

    @patch('os.system')
    def test_vulnerability(self, mock_os_system):
        malicious_link = 'google.com%3B%20ls'
        response = self.app.get(f'/ping?link={malicious_link}')

        # Vulnerability: Command injection allowed
        self.assertEqual(response.status_code, 200)
        # Note: Flask will decode it back to 'google.com; ls'
        self.assertEqual(response.data.decode(), 'google.com; ls')
        mock_os_system.assert_called_with('ping google.com; ls')

if __name__ == '__main__':
    unittest.main()