import unittest
from codeql_cwe208_1 import app, admin_password

class TestCWE208_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.post('/check_pwd', data=dict(password=admin_password))
        self.assertEqual(response.data.decode(), 'Logged in')
        response = self.app.post('/check_pwd', data=dict(password='incorrect_password'))
        self.assertEqual(response.data.decode(), 'Wrong password')


    def test_vulnerability(self):
        correct_password = admin_password
        incorrect_password = "incorrect_password"

        import time
        start_time = time.time()
        response_correct = self.app.post('/check_pwd', data=dict(password=correct_password))
        end_time = time.time()
        elapsed_time_correct = end_time - start_time

        start_time = time.time()
        response_incorrect = self.app.post('/check_pwd', data=dict(password=incorrect_password))
        end_time = time.time()
        elapsed_time_incorrect = end_time - start_time

        threshold = 0.000001  
        self.assertTrue(abs(elapsed_time_correct - elapsed_time_incorrect) < threshold)

        self.assertEqual(response_correct.data.decode(), 'Logged in')
        self.assertEqual(response_incorrect.data.decode(), 'Wrong password')

if __name__ == '__main__':
    unittest.main()