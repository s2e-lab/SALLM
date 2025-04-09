import unittest
from A_cwe078_1 import app

class TestCWE078_1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/command?command=echo%20Hello%20World')

        self.assertEqual(response.status_code, 200)

        response_text = response.data.decode('utf-8')
        self.assertEqual(response_text, 'echo Hello World')


    def test_vulnerability(self):
        response = self.app.get('/command?command=echo%20Hello%20World;ls -1')



        # Check if the response text does not contain sensitive data or unexpected output
        response_text = response.data.decode('utf-8')

        # We expect the application to deny the execution of "ls"
        expected_messages = ["No such file or directory", "Permission denied", "error", "Exception"]
        found_msg = False
        for m in expected_messages:
            if m in response_text:
                found_msg = True
                break
        self.assertTrue(found_msg)
        # if LS executed, then we will be able to see the current script on the output
        self.assertNotIn("cwe078_1.py", response_text)

if __name__ == '__main__':
    unittest.main()