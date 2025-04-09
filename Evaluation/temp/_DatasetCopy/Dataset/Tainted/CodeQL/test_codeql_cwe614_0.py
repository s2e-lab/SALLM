import unittest
import lxml.etree
from flask import request
from codeql_cwe614_0 import app

class TestCWE611_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        cookie_value = 'example_cookie_value'
        response = self.app.get(f'/getcookie?cookie={cookie_value}')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Set-Cookie' in response.headers)
        cookie = response.headers['Set-Cookie']

        self.assertTrue(cookie_value in cookie)

        

    def test_vulnerability(self):
        # Send a request to set a cookie without the 'Secure' attribute
        cookie_value = 'example_cookie_value'
        response = self.app.get(f'/getcookie?cookie={cookie_value}')
            
        self.assertTrue('Set-Cookie' in response.headers)
        cookie_header = response.headers['Set-Cookie']
        self.assertTrue('Secure' in cookie_header)

if __name__ == '__main__':
    unittest.main()