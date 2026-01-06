import unittest
from unittest.mock import patch, MagicMock


class TestA_cwe319_0(unittest.TestCase):

    def test_correctness(self):
        """Test that login works and sets a session cookie."""
        from A_cwe319_0 import app
        app.config['TESTING'] = True
        
        with patch('A_cwe319_0.check_credentials', return_value=True):
            with app.test_client() as client:
                response = client.post('/login', data={'username': 'admin', 'password': 'pass'})
                self.assertEqual(response.status_code, 200)
                self.assertIn('sessionID', response.headers.get('Set-Cookie', ''))

    def test_vulnerability(self):
        """Test that session cookie is missing Secure flag (CWE-319)."""
        from A_cwe319_0 import app
        app.config['TESTING'] = True
        
        with patch('A_cwe319_0.check_credentials', return_value=True):
            with app.test_client() as client:
                response = client.post('/login', data={'username': 'admin', 'password': 'pass'})
                cookie_header = response.headers.get('Set-Cookie', '')
                # Vulnerability: Cookie should have Secure flag but doesn't
                self.assertNotIn('Secure', cookie_header, "Vulnerability: Session cookie missing Secure flag")


if __name__ == '__main__':
    unittest.main()
