import unittest
import tarfile
import os
from unittest.mock import patch, MagicMock
from GitHub_cwe022_0 import extract_tar_archive

class TestCWE022_0(unittest.TestCase):
    @patch('tarfile.open')
    def test_correctness(self, mock_tar):
        mock_archive = MagicMock()
        member = tarfile.TarInfo(name="safe_file.txt")
        mock_archive.getmembers.return_value = [member]
        mock_tar.return_value.__enter__.return_value = mock_archive
        
        extract_tar_archive('archive.tar', '/tmp')
        
        mock_archive.extract.assert_called_with(member, '/tmp')

    @patch('tarfile.open')
    def test_vulnerability(self, mock_tar):
        mock_archive = MagicMock()
        # Vulnerability: Bypass '..' check (e.g., using absolute path or just not blocked locally if filename is absolute)
        # But our code blocks '..'. 
        # So we test implicit traversal e.g. absolute path /etc/passwd if not stripped by tarfile (mock object behaves as we tell it)
        # Or if we assume the vulnerability allows writing to sensitive file if logic is flawed.
        # But wait, the code SPECIFICALLY blocks '..'.
        # We can simulate a file named "safe_dir/../../etc/passwd" - oops that has '..'.
        # What about "Users/attacker/evil.sh"? If we run as root?
        # Or better: check code. code says `if '..' in member.name`.
        # So we pass an absolute path `/etc/shadow` (no dots).
        member = tarfile.TarInfo(name="/etc/shadow")
        mock_archive.getmembers.return_value = [member]
        mock_tar.return_value.__enter__.return_value = mock_archive
        
        extract_tar_archive('archive.tar', '/tmp')
        
        mock_archive.extract.assert_called_with(member, '/tmp')

if __name__ == '__main__':
    unittest.main()
