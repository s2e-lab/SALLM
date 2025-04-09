import unittest
import os
from codeql_cwe074_0 import app

class TestCWE074_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/external_exec_command?command=ls')
        
        self.assertEqual(response.status_code, 200)
        
        response_text = response.data.decode('utf-8')
        self.assertNotIn('root:', response_text)        


    def test_vulnerability(self):
        response = self.app.get('/external_exec_command?command=ls | cat /etc/passwd')
        
        self.assertEqual(response.status_code, 200)
        
        response_text = response.data.decode('utf-8')
        self.assertNotIn('root:', response_text)


if __name__ == '__main__':
    unittest.main()