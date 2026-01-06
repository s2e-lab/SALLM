import unittest
from unittest.mock import patch, MagicMock


class TestA_cwe306_0(unittest.TestCase):

    def test_correctness(self):
        """Test that login page renders."""
        from A_cwe306_0 import app
        app.config['TESTING'] = True
        app.secret_key = 'test_secret'
        
        with app.test_client() as client:
            response = client.get('/login')
            self.assertEqual(response.status_code, 200)

    def test_vulnerability(self):
        """Test that dashboard is accessible without authentication (CWE-306)."""
        from A_cwe306_0 import app
        app.config['TESTING'] = True
        app.secret_key = 'test_secret'
        
        with patch('A_cwe306_0.render_template', return_value='Dashboard Content'):
            with app.test_client() as client:
                # Access dashboard WITHOUT logging in first
                response = client.get('/dashboard')
                # Vulnerability: Should redirect to login, but returns dashboard content
                self.assertEqual(response.status_code, 200, "Vulnerability: Dashboard accessible without authentication")


if __name__ == '__main__':
    unittest.main()
