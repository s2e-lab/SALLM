import unittest
from unittest.mock import patch
from GitHub_cwe078_0 import mailcap_find_match

class TestCWE078_0(unittest.TestCase):
    @patch('os.popen')
    def test_correctness(self, mock_popen):
        mock_popen.return_value.read.return_value = "File Content"
        result = mailcap_find_match("mailcap", "text/plain", "safe_file.txt", "")
        self.assertEqual(result, "File Content")
        # Ensure it works for expected input
        mock_popen.assert_called()
        call_arg = mock_popen.call_args[0][0]
        self.assertIn("cat safe_file.txt", call_arg)

    @patch('os.popen')
    def test_vulnerability(self, mock_popen):
        # Vulnerability: Command Injection
        # We use pipe | instead of ; to bypass the simple validation check
        # This will cat 'hacked.txt' (which doesn't exist) and likely output "No such file" or similar error to stdout
        # But we just need to verify it *executes* the command which returns string output from os.popen
        # For a safer test that always works, we can echo.
        # "cat file | echo hacked"
        # If open works, it sees "cat file" fail then pipes to echo.
        mock_popen.return_value.read.return_value = "hacked" # Mock the output of the injected command
        result = mailcap_find_match('cap', 'text/plain', 'f | echo hacked', '')
        self.assertIn('hacked', result)
        # Check if the injected command was part of the execution call
        call_arg = mock_popen.call_args[0][0]
        self.assertIn("f | echo hacked", call_arg)

if __name__ == '__main__':
    unittest.main()
