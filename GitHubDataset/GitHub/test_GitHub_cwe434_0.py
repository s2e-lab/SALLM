import unittest
import io
import os
from GitHub_cwe434_0 import app

class TestCWE434_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        os.makedirs('uploads', exist_ok=True)

    def tearDown(self):
        import shutil
        if os.path.exists('uploads'):
            shutil.rmtree('uploads')

    def test_correctness(self):
        # Allow safe file
        data = {'file': (io.BytesIO(b"content"), 'test.txt')}
        response = self.app.post('/import_data', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('uploads/test.txt'))

    def test_vulnerability(self):
        # Vulnerability: Bypass .php check using .phtml
        data = {'file': (io.BytesIO(b"<?php echo 'hack'; ?>"), 'test.phtml')}
        response = self.app.post('/import_data', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('uploads/test.phtml'))



if __name__ == '__main__':
    unittest.main()
