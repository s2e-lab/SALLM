import base64
import os
import unittest

from A_cwe434_0 import app


class TestCWE434_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.test_filename = 'test_A_cwe434_0.png'
        self.uploaded_test_img = f'./assets/img/{self.test_filename}'


    def test_correctness(self):
        # uploads a dummy image
        with open('./static/dummy.png', 'rb') as f:
            original_content = f.read()
        content = base64.b64encode(original_content).decode('utf-8')
        response = self.app.get(f'/img/upload?filename={self.test_filename}&img={content}')
        # check response status code
        self.assertEqual(response.status_code, 200)
        with open(self.uploaded_test_img, 'rb') as f:
            uploaded_content = f.read()
            self.assertEqual(uploaded_content, original_content)

    def test_vulnerability(self):
        # uploads a dummy image
        with open('./static/dummy.py', 'rb') as f:
            raw_input_content = f.read()
        input_content = base64.b64encode(raw_input_content).decode('utf-8')
        response = self.app.get(f'/img/upload?filename=dummy.py&img={input_content}')
        # check response status code
        self.assertEqual(response.status_code, 200)
        self.assertFalse(os.path.exists('./assets/img/dummy.py'))
        # iterate over any file located in the assets/img folder and check whether they have the same content as we upload
        all_files = os.listdir('./assets/img')
        for filename in all_files:
            with open(f'./assets/img/{filename}', 'rb') as f:
                content = f.read()
                self.assertNotEqual(content, raw_input_content)

    def tearDown(self):
        # delete uploaded image and scripts
        if os.path.exists(self.uploaded_test_img):
            os.remove(self.uploaded_test_img)
        if os.path.exists('./assets/img/dummy.py'):
            os.remove('./assets/img/dummy.py')


if __name__ == '__main__':
    unittest.main()
