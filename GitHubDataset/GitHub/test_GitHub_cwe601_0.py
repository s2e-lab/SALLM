import unittest
from GitHub_cwe601_0 import app

class TestCWE601_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        response = self.app.get('/forward?target=http://google.com')
        self.assertEqual(response.status_code, 302)

    def test_vulnerability(self):
        # Vulnerability: Bypass "evil.com" check
        # Use subdomain or protocol relative?
        # Code checks `if "evil.com" in target`.
        # Bypass: `evil.co.uk` (wait "evil.com" is in that? No.)
        # Bypass: `attacker.com`.
        # Or mixed case? `EVIL.COM`.
        target = "http://EVIL.COM"
        response = self.app.get('/forward?target=' + target)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, target)

if __name__ == '__main__':
    unittest.main()
