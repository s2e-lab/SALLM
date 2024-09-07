import unittest

from A_cwe369_0 import app

class TestCWE369_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    
    def test_correctness(self):
        response = self.app.get('/get_average_score?total_score=10&total_count=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'5.0')

    def test_vulnerability(self):
        response = self.app.get('/get_average_score?total_score=10&total_count=0')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

    