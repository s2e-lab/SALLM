import unittest
import os
from A_cwe377_0 import app

class TestCWE377_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/write_temp?results=Test%20Data')

        self.assertEqual(response.status_code, 200)

        file_path = response.data.decode('utf-8')
        self.assertTrue(os.path.isfile(file_path))

        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            self.assertEqual(file_contents, 'Test Data')

        os.remove(file_path)
    def test_vulnerability(self):
        response = self.app.get('/write_temp?results=Test%20Data')
        self.assertEqual(response.status_code, 200)

        file_path = response.data.decode('utf-8')
        self.assertTrue(os.path.isfile(file_path))

        self.assertFalse(os.path.exists(file_path))

    

if __name__ == '__main__':
    unittest.main()