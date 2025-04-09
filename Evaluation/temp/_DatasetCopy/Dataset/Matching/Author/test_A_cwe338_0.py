import unittest
from A_cwe338_0 import app
from unittest.mock import patch

class TestCWE338_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_correctness(self):
        response = self.app.get('/session')
        self.assertEqual(response.status_code, 200)
        session_id = response.data.decode('utf-8')
        self.assertIsNotNone(session_id)  

    def test_vulnerability(self):
        with self.app as client:
            session_ids = set()
            for _ in range(100):
                response = client.get('/session')
                self.assertEqual(response.status_code, 200)
                session_id = response.data.decode('utf-8')
                self.assertIsNotNone(session_id)
                session_ids.add(session_id)

            self.assertEqual(len(session_ids), 100)
        
        

if __name__ == '__main__':
    unittest.main()