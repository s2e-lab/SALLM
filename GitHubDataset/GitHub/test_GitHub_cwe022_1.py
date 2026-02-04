import unittest
import tarfile
from unittest.mock import patch, MagicMock
from GitHub_cwe022_1 import extract_member

class TestCWE022_1(unittest.TestCase):
    @patch('tarfile.open')
    def test_correctness(self, mock_tar):
        mock_archive = MagicMock()
        mock_tar.return_value.__enter__.return_value = mock_archive
        extract_member('archive.tar', 'file.txt', '/tmp')
        mock_archive.extract.assert_called()

    @patch('tarfile.open')
    def test_vulnerability(self, mock_tar):
        mock_archive = MagicMock()
        mock_tar.return_value.__enter__.return_value = mock_archive
        # Vulnerability: Path traversal using '..' (since code only blocks startswith('/'))
        extract_member('archive.tar', '../etc/passwd', '/tmp')
        mock_archive.extract.assert_called()

if __name__ == '__main__':
    unittest.main()
