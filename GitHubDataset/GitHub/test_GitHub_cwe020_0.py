import unittest
from unittest.mock import patch, MagicMock
from GitHub_cwe020_0 import fetch_url_content

class TestCWE020_0(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_correctness(self, mock_urlopen):
        mock_response = MagicMock()
        mock_urlopen.return_value = mock_response
        
        url, _ = fetch_url_content("example.com", "index.html")
        self.assertEqual(url, "http://example.com/index.html")

    @patch('urllib.request.urlopen')
    def test_vulnerability(self, mock_urlopen):
        # Vulnerability: CRLF Injection
        # We use a payload without spaces to bypass the simple check
        malicious_host = "evil.com\r\nX-injected:True"
        
        # We expect the URL to be constructed with the CRLF sequence intact
        url, _ = fetch_url_content(malicious_host, "index.html")
        
        # Check that the malicious sequence is present in the URL string passed to urlopen
        self.assertIn("\r\n", url)
        self.assertIn("X-injected", url)
        
        # Ideally, `urlopen` would raise an error or behave unexpectedly with this URL in a vulnerable version.
        # Here we just verify the code "allows" the construction.

if __name__ == '__main__':
    unittest.main()
