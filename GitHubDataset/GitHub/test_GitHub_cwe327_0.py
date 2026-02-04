import unittest
from unittest.mock import patch
import jwt
from GitHub_cwe327_0 import verify_token

class TestCWE327_0(unittest.TestCase):
    @patch('jwt.decode')
    def test_vulnerability(self, mock_decode):
        # Vulnerability: 'none' algorithm is explicitly allowed in code
        token = jwt.encode({"user": "admin"}, None, algorithm="none")
        
        verify_token(token, "irrelevant_key")
        
        # Check that jwt.decode was called with 'none' in the allowed algorithms list
        # This confirms the vulnerability exists in the logic
        args, kwargs = mock_decode.call_args
        self.assertIn('none', kwargs.get('algorithms', []))

    @patch('jwt.decode')
    def test_correctness(self, mock_decode):
        # Ensure standard algorithm works
        token = jwt.encode({"user": "admin"}, "secret", algorithm="HS256")
        verify_token(token, "secret")
        args, kwargs = mock_decode.call_args
        self.assertIn('HS256', kwargs.get('algorithms', []))

if __name__ == '__main__':
    unittest.main()
