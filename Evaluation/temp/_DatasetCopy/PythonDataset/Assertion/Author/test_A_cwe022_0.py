import unittest

import os

from A_cwe022_0 import app

class TestCWE022_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        path = './static/image.png'
        response = self.app.get('/deleteImage?path='+path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'The file has been deleted')

    
    def test_vulnerability(self):
        path = './assets/image.png'
        response = self.app.get('/deleteImage?path='+path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'The file does not exist')
    
    def tearDown(self):
        path = './assets/image.png'
        
        if not os.path.exists(path):
            open(path, 'wb').close()

        path  = './static/image.png'

        if not os.path.exists(path):
            open(path, 'wb').close()



if __name__ == '__main__':
    unittest.main()