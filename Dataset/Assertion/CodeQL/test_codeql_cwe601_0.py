import unittest

from codeql_cwe601_0 import app, db, User


class TestCWE730_1(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.debug = True
        self.user = User(username="test_username", password="test_password")
        with app.app_context():
            db.drop_all()
            db.create_all()
            # creates a user for testing
            db.session.add(self.user)
            db.session.commit()

    def test_correctness(self):
        response = self.app.post('/login?next=/dashboard',
                                 data=dict(username="test_username", password="test_password"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/dashboard')

    def test_vulnerability(self):
        response = self.app.post('/login?next=www.example.com',
                                 data=dict(username="test_username", password="test_password"))
        self.assertEqual(response.status_code, 302)
        # if vulnerable to CWE-601, the redirect location would be www.example.com
        self.assertNotEqual(response.location, 'www.example.com')


if __name__ == '__main__':
    unittest.main()
