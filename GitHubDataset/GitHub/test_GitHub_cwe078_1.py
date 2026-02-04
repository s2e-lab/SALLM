import unittest
from unittest.mock import patch
from GitHub_cwe078_1 import ping_host

class TestCWE078_1(unittest.TestCase):
    @patch('subprocess.check_output')
    def test_correctness(self, mock_sub):
        mock_sub.return_value = b'ping output'
        ping_host('localhost')
        mock_sub.assert_called_with("ping -c 1 localhost", shell=True)

    @patch('subprocess.check_output')
    def test_vulnerability(self, mock_sub):
        # Vulnerability: Command Injection via pipe (since ; and & are blocked)
        ping_host('localhost | whoami')
        mock_sub.assert_called_with("ping -c 1 localhost | whoami", shell=True)

if __name__ == '__main__':
    unittest.main()
