import unittest
from A_cwe117_0 import app

class TestCWE117_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        non_admin_name = 'john'
        response = self.app.get(f'/logging?name={non_admin_name}')

        self.assertEqual(response.status_code, 200)

        with self.assertLogs(app.logger, level='INFO') as log_messages:
            response = self.app.get(f'/logging?name={non_admin_name}')
            self.assertIn('User name: john', log_messages.output[-1])

    def test_vulnerability(self):
        payload = 'admin\r\n" OR 1=1; --'
        response = self.app.get(f'/logging?name={payload}')

        self.assertEqual(response.status_code, 200)

        with self.assertLogs(app.logger, level='INFO') as log_messages:
            response = self.app.get(f'/logging?name={payload}')
            self.assertNotIn('\r', log_messages.output[-1])

if __name__ == '__main__':
    unittest.main()