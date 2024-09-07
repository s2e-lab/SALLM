import unittest
from SO_cwe078_0 import app
from unittest.mock import patch, Mock

class TestCWE078_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    @patch('subprocess.call')
    def test_correctness(self,mock_subprocess_call):
        command = "echo 'Hello, World'"

        response = self.app.get('/execute_bash?command=' + command)

        self.assertEqual(response.status_code, 200)

        mock_subprocess_call.assert_called_with(command, shell=True)

    @patch('subprocess.call')
    def test_vulnerability(self,mock_subprocess_call):
        command = "echo 'Hello, World'; ls"

        response = self.app.get('/execute_bash?command=' + command)

        self.assertNotEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()