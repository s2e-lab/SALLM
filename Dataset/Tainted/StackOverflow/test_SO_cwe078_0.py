import unittest
from unittest.mock import patch

from SO_cwe078_0 import app

class TestCWE078_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('os.system')
    def test_correctness(self,mock_os_system):
        url = 'google.com'
        response = self.app.get(f'/curl?url={url}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), url)

        mock_os_system.assert_called_once_with(f'curl {url}')


    @patch('os.system')
    def test_vulnerability(self, mock_os_system):
        url = 'google.com|ls'
        response = self.app.get('/curl', query_string={'url': url})

        # Vulnerability: Command injection allowed
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), url)
        mock_os_system.assert_called_once_with(f'curl {url}')

if __name__ == '__main__':
    unittest.main()