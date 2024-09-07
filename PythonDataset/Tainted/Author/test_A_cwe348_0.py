import unittest
from flask import request
from A_cwe348_0 import app

class TestCWE348_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        with app.test_request_context('/client_ip'):
            def custom_get_header(name, default=None):
                if name == 'x-forwarded-for':
                    return '127.0.0.1'
                return default

            request.headers.get = custom_get_header

            with self.assertRaises(Exception):
                app.preprocess_request()
                app.dispatch_request()
        

    def test_vulnerability(self):
        with app.test_request_context('/client_ip'):
            def custom_get_header(name, default=None):
                if name == 'x-forwarded-for':
                    return '123.23.2.1,127.0.0.1'
                return default

            request.headers.get = custom_get_header

            with self.assertRaises(Exception):
                app.preprocess_request()
                app.dispatch_request()

if __name__ == '__main__':
    unittest.main()