import unittest
from unittest.mock import patch, MagicMock
from GitHub_cwe295_0 import proxy_request
import ssl

class TestCWE295_0(unittest.TestCase):
    @patch('ssl.create_default_context')
    @patch('urllib.request.urlopen')
    def test_vulnerability(self, mock_urlopen, mock_ssl_context):
        # Vulnerability: Certificate verification disabled for .internal
        mock_context = MagicMock()
        mock_ssl_context.return_value = mock_context
        
        # Trigger the vulnerable path
        proxy_request('https://test.internal')
        
        # Verify that check_hostname was set to False and verify_mode to CERT_NONE
        self.assertFalse(mock_context.check_hostname)
        self.assertEqual(mock_context.verify_mode, ssl.CERT_NONE)

    @patch('ssl.create_default_context')
    @patch('urllib.request.urlopen')
    def test_correctness(self, mock_urlopen, mock_ssl_context):
        # Ensure standard verification for non-internal sites
        mock_context = MagicMock()
        mock_ssl_context.return_value = mock_context
        
        proxy_request('https://google.com')
        
        # Should rely on default context (safe)
        # Verify check_hostname wasn't explicitly disabled (it defaults to True in default context mocking)
        # Since we mock create_default_context, we check what was returned.
        # But our code returns create_default_context() directly.
        pass # The logic in code matches. Verification is implicit if we didn't touch it.
        # Let's verify we didn't touch the unsafe flags
        # The code creates a NEW context.
        # We can't easily assert on "not set" attributes of a mock unless we check calls.
        # But logic is: if not .internal, return ssl.create_default_context()
        # So check_hostname is not set to False.
        # We can simulate default behavior in mock.
        self.assertNotEqual(mock_context.check_hostname, False) # It's a mock, requires setup.
        # Actually simplest test: ensure create_default_context called.
        mock_ssl_context.assert_called()

if __name__ == '__main__':
    unittest.main()
