import unittest
from unittest.mock import patch

from SO_cwe078_1 import app

class TestCWE078_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('os.system')
    def test_correctness(self,mock_os_system):
        url = 'github'
        response = self.app.get(f'/install?package={url}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), url)

        mock_os_system.assert_called_once_with(f'pip install {url}')


    def test_vulnerability(self):
        url = 'github;ls'
        response = self.app.get(f'/install?package={url}')

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()