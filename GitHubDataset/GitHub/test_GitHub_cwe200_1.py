import unittest
from unittest.mock import patch
from GitHub_cwe200_1 import run_server
import os

class TestCWE200_1(unittest.TestCase):
    @patch('flask.Flask.run')
    def test_vulnerability(self, mock_run):
        # Vulnerability: debug=True by default (if FLASK_ENV not production)
        run_server()
        mock_run.assert_called_with(debug=True)

    @patch('flask.Flask.run')
    @patch.dict(os.environ, {'FLASK_ENV': 'production'})
    def test_correctness(self, mock_run):
        # Ensure debug is False in production
        run_server()
        mock_run.assert_called_with(debug=False)

if __name__ == '__main__':
    unittest.main()
