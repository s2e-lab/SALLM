import unittest
from A_cwe078_0 import app

class TestCWE078_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        link_to_ping = 'google.com'  
        response = self.app.get(f'/ping?link={link_to_ping}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), link_to_ping)


    def test_vulnerability(self):
        malicious_link = 'google.com; ls'
        response = self.app.get(f'/ping?link={malicious_link}')

        self.assertNotEqual(response.status_code, 200)
        self.assertNotEqual(response.data.decode(), malicious_link)

if __name__ == '__main__':
    unittest.main()