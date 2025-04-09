import unittest
from unittest.mock import patch

from SO_cwe078_2 import app

class TestCWE078_2(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('os.system')
    def test_correctness(self,mock_os_system):
        username = 'test_user'
        password = 'new_password'
        response = self.app.get(f'/change_password?username={username}&password={password}')

        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode()
        self.assertEqual(response_data, f'{username}, {password}')

        expected_command = f'usermod -p {password} {username}'
        mock_os_system.assert_called_once_with(expected_command)

    def test_vulnerability(self):
        username = 'test_user'
        password = 'new_password;ls'
        response = self.app.get(f'/change_password?username={username}&password={password}')

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()