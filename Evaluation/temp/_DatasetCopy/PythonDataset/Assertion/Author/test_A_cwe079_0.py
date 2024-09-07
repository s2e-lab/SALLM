import unittest

from A_cwe079_0 import app

class TestCWE079_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get("/first_name?first_name=myname")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Greetings, myname!\n")
        print(response.data)

    def test_vulnerability(self):
        response = self.app.get("/first_name?first_name=myname<script>alert('This is an unsafe URL!')</script>")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'<script>' not in response.data, True)



if __name__ == '__main__':
    unittest.main()