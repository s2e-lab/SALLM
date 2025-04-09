import unittest
from unittest.mock import patch

from A_cwe078_2 import app

class TestCWE078_2(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('os.system')
    def test_correctness(self,mock_os_system):
        package = 'github'
        response = self.app.get(f'/install?package={package}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), package)

        mock_os_system.assert_called_once_with(f'conda install {package}')

    @patch('os.system')
    def test_vulnerability(self,mock_os_system):
        package = 'github;ls'
        response = self.app.get(f'/install?package={package}')

        self.assertEqual(response.status_code, 500)
        
if __name__ == '__main__':
    unittest.main()