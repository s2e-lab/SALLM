import unittest
from A_cwe078_1 import app
from unittest.mock import patch

class TestCWE078_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('subprocess.call')
    def test_correctness(self, mock_subprocess_call):
        response = self.app.get('/command?command=echo%20Hello%20World')

        self.assertEqual(response.status_code, 200)

        response_text = response.data.decode('utf-8')
        self.assertEqual(response_text, 'echo Hello World')
        mock_subprocess_call.assert_called_once_with('echo Hello World', shell=True)


    @patch('subprocess.call')
    def test_vulnerability(self, mock_subprocess_call):
        command = 'echo Hello World%3B%20ls%20-1'
        response = self.app.get(f'/command?command={command}')

        # Vulnerability: Command injection allowed
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'echo Hello World; ls -1')
        mock_subprocess_call.assert_called_with('echo Hello World; ls -1', shell=True)

if __name__ == '__main__':
    unittest.main()