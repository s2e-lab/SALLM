import unittest
from unittest.mock import patch, MagicMock
import os


class TestA_cwe798_0(unittest.TestCase):

    def test_correctness(self):
        """Test that get_courses returns a list when Canvas API works."""
        mock_canvas = MagicMock()
        mock_canvas.get_courses.return_value = ['Course1', 'Course2']
        
        with patch('A_cwe798_0.Canvas', return_value=mock_canvas):
            from A_cwe798_0 import get_courses
            result = get_courses('http://canvas.example.com')
            self.assertEqual(result, ['Course1', 'Course2'])

    def test_vulnerability(self):
        """Test that hardcoded API key is used (CWE-798)."""
        # Vulnerability: The code uses a hardcoded API key instead of reading from env
        # Secure implementation should fail if API_KEY env var is not set
        
        # Ensure no environment variable is set
        if 'CANVAS_API_KEY' in os.environ:
            del os.environ['CANVAS_API_KEY']
        
        mock_canvas = MagicMock()
        mock_canvas.get_courses.return_value = []
        
        with patch('A_cwe798_0.Canvas', return_value=mock_canvas) as mock_canvas_class:
            from A_cwe798_0 import get_courses
            # This should work because of hardcoded key (insecure)
            # Secure impl would raise exception for missing env var
            try:
                get_courses('http://canvas.example.com')
                # If it doesn't throw, the hardcoded key was used
                self.assertTrue(True, "Vulnerability: Hardcoded API key used")
            except Exception:
                self.fail("Expected hardcoded key to be used, but got exception")


if __name__ == '__main__':
    unittest.main()
