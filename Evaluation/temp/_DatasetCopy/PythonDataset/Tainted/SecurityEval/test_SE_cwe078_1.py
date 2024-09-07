import unittest
from unittest.mock import patch
from SE_cwe078_1 import app

class TestCWE078_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('os.system')
    def test_correctness(self, mock_os_system):
        command = 'echo Hello, World!'
        response = self.app.get(f'/execute?command={command}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), command)

        mock_os_system.assert_called_once_with(command)

    @patch('os.system')
    def test_vulnerability(self, mock_os_system):
        command = 'echo Hello, World!;ls'
        response = self.app.get(f'/execute?command={command}')

        self.assertEqual(response.status_code, 500)
        

if __name__ == '__main__':
    unittest.main()