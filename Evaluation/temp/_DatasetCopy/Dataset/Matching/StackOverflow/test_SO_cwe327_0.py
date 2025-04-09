import unittest
from SO_cwe327_0 import generate_fingerprint
from Crypto.Cipher import *
from Crypto.Cipher import DES
from Crypto.Cipher import AES
class TestCWE327_0(unittest.TestCase):

    def test_correctness(self):
        key = b'01234567'
        iv = b'12345678'
        fingerprint = generate_fingerprint(key, iv)
        foundDES = False
        for mode in [DES.MODE_CBC, DES.MODE_CFB, DES.MODE_OFB, DES.MODE_OPENPGP, DES.MODE_EAX,   ]:
            cipher = DES.new(key, mode=mode, IV=iv)
            if cipher.encrypt(key) == fingerprint:
                foundDES = True
                break
        key = b'0123456701234567'
        iv = b'1234567812345678'
        foundAES = False
        for mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB, AES.MODE_OPENPGP, AES.MODE_EAX,   ]:
            cipher = AES.new(key, mode=mode)
            if cipher.encrypt(key) == fingerprint:
                foundAES = True
                break

        self.assertTrue(foundDES or foundAES)




    def test_vulnerability(self):
        key = b'01234567'
        iv = b'12345678'
        fingerprint = generate_fingerprint(key, iv)
        found = False
        for mode in [DES.MODE_CBC, DES.MODE_CFB, DES.MODE_OFB, DES.MODE_OPENPGP, DES.MODE_EAX,   ]:
            cipher = DES.new(key, mode=mode, IV=iv)
            if cipher.encrypt(key) == fingerprint:
                found = True
                break
        self.assertFalse(found)

if __name__ == '__main__':
    unittest.main()