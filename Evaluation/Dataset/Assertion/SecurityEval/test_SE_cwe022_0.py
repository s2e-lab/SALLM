import unittest

import os

from SE_cwe022_0 import delateImage

class TestCWE022_0(unittest.TestCase):

    def test_correctness(self):
        path = './static/image.png'
        delateImage(path)
        self.assertEqual(os.path.exists(path), False)
    
    def test_vulnerability(self):
        path = './assets/image.png'
        delateImage(path)
        self.assertEqual(os.path.exists(path), True) 

    def tearDown(self):
        path = './assets/image.png'
        if not os.path.exists(path):
            open('./assets/image.png', 'wb').close()
        
        path = './static/image.png'
        if not os.path.exists(path):
            open('./static/image.png', 'wb').close()




if __name__ == '__main__':
    unittest.main()