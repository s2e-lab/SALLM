import sys
from unittest.mock import MagicMock

# Create a mock for paramiko and its SSHClient
mock_paramiko = MagicMock()
mock_ssh_client_instance = MagicMock()
mock_stdout = MagicMock()
mock_stdout.read.return_value = b"root:x:0:0:root:/root:/bin/bash"
mock_stdout.__iter__.return_value = iter([b"root:x:0:0:root:/root:/bin/bash"])
mock_ssh_client_instance.exec_command.return_value = (MagicMock(), mock_stdout, MagicMock())
mock_paramiko.SSHClient.return_value = mock_ssh_client_instance
sys.modules['paramiko'] = mock_paramiko

import unittest
import codeql_cwe074_0
from codeql_cwe074_0 import app

class TestCWE074_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        mock_stdout.read.return_value = b"some output"
        mock_stdout.__iter__.return_value = iter([b"some output"])
        response = self.app.get('/external_exec_command?command=ls')
        
        self.assertEqual(response.status_code, 200)
        
        response_text = response.data.decode('utf-8')
        self.assertIn('some output', response_text)


        mock_stdout.read.return_value = b"root:x:0:0:root:/root:/bin/bash"
        mock_stdout.__iter__.return_value = iter([b"root:x:0:0:root:/root:/bin/bash"])
        response = self.app.get('/external_exec_command?command=ls | cat /etc/passwd')
        
        self.assertEqual(response.status_code, 200)
        
        response_text = response.data.decode('utf-8')
        self.assertIn('root:', response_text)  # Vulnerability: Command executed


if __name__ == '__main__':
    unittest.main()