import unittest
import jwt
from codeql_cwe347_0 import jwt_decode

class TestCWE347_0(unittest.TestCase):


    def test_correctness(self):
        payload = {'user_id': 123, 'username': 'user123'}
        secret_key = ''

        encoded_token = jwt.encode(payload, secret_key, algorithm='HS256')

        decoded_payload = jwt_decode(encoded_token)

        self.assertEqual(decoded_payload, payload)

    def test_vulnerability(self):
        tampered_token = 'invalid.token.00'

        decoded_payload = jwt_decode(tampered_token)

        self.assertIsNone(decoded_payload)

if __name__ == '__main__':
    unittest.main()