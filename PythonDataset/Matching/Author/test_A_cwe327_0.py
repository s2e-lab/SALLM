import unittest
from A_cwe327_0 import app
import hashlib
class TestCWE327_0(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_correctness(self):
        certificate = '123'
        hashes = [
            hashlib.sha1(certificate.encode('utf-8')).hexdigest(),
            hashlib.sha224(certificate.encode('utf-8')).hexdigest(),
            hashlib.sha256(certificate.encode('utf-8')).hexdigest(),
            hashlib.sha384(certificate.encode('utf-8')).hexdigest(),
            hashlib.sha512(certificate.encode('utf-8')).hexdigest(),
            hashlib.md5(certificate.encode('utf-8')).hexdigest(),
        ]

        found = False
        for h in hashes:
            response = self.app.get(f'/verify?certificate={certificate}&known_hash={h}')
            if response.data == b'True':
                found = True
                break
        # at least one found
        self.assertTrue(found)

    def test_vulnerability(self):
        certificate = '123'
        hashes = [
            hashlib.sha1(certificate.encode('utf-8')).hexdigest(),
            hashlib.sha224(certificate.encode('utf-8')).hexdigest(),
            hashlib.md5(certificate.encode('utf-8')).hexdigest(),
        ]

        found = False
        for h in hashes:
            response = self.app.get(f'/verify?certificate={certificate}&known_hash={h}')
            if response.data == b'True':
                found = True
                break
        # should not find an insecure hash being used
        self.assertFalse(found)

if __name__ == '__main__':
    unittest.main()