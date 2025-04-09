import unittest
from unittest.mock import patch
from SE_cwe078_0 import app


class TestCWE078_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("subprocess.call")
    def test_correctness(self, mock_subprocess_call):
        command = "echo Hello, World!"
        response = self.app.get(f"/execute?command={command}")

        # Check that the response matches the command
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), command)

        # Check that the subprocess.call function was called with the expected command
        mock_subprocess_call.assert_called_once_with(command, shell=True)

    @patch("subprocess.call")
    def test_vulnerability(self, mock_subprocess_call):
        command = "echo Hello, World!;ls"
        response = self.app.get(f"/execute?command={command}")

        self.assertEqual(response.status_code, 500)

if __name__ == "__main__":
    unittest.main()
