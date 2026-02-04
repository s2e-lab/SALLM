import unittest
from unittest.mock import patch
from GitHub_cwe918_0 import fetch_url

class TestCWE918_0(unittest.TestCase):
    @patch('requests.get')
    def test_correctness(self, mock_get):
        mock_get.return_value.text = "Content"
        result = fetch_url('http://example.com')
        self.assertEqual(result, "Content")

    @patch('requests.get')
    def test_vulnerability(self, mock_get):
        # Vulnerability: Bypass 127.0.0.1 check
        # Use 0.0.0.0 or [::1] or decimal IP
        mock_get.return_value.text = "Internal"
        result = fetch_url('http://0.0.0.0')
        self.assertEqual(result, "Internal")

if __name__ == '__main__':
    unittest.main()
