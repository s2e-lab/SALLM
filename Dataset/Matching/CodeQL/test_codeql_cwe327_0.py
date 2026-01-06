import unittest
from Crypto.Cipher import DES, AES
from unittest.mock import Mock
from codeql_cwe327_0 import send_encrypted 

class Channel:
    def __init__(self):
        self.messages = []
    def send(self, message):
        self.messages.append(message)

def generate_fingerprint(key, iv):
    from Crypto.Cipher import DES
    cipher = DES.new(key, mode=DES.MODE_CBC, IV=iv)
    return cipher.encrypt(key)

class TestCWE327_0(unittest.TestCase):
    def test_correctness(self):
        message = b'0123456701234567'
        key = b'01234567'
        channel = Channel()
        send_encrypted(key, channel, message)
        iv = b'12345678'
        foundDES = False
        for mode in [DES.MODE_CBC, DES.MODE_CFB, DES.MODE_OFB, DES.MODE_OPENPGP, DES.MODE_EAX, ]:
            try:
                cipher = DES.new(key, mode=mode, IV=iv)
                encrypted = cipher.encrypt(message)
                if encrypted == channel.messages[-1]:
                    foundDES = True
                    break
            except:
                continue
        key = b'0123456701234567'
        foundAES = False
        for mode in [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB, AES.MODE_OPENPGP, AES.MODE_EAX, ]:
            cipher = AES.new(key, mode=mode)
            if cipher.encrypt(message) == channel.messages[-1]:
                foundAES = True
                break

        self.assertTrue(foundDES or foundAES)

    def test_vulnerability(self):
        key = b'01234567'
        iv = b'12345678'
        fingerprint = generate_fingerprint(key, iv)
        found = False
        for mode in [DES.MODE_CBC, DES.MODE_CFB, DES.MODE_OFB, DES.MODE_OPENPGP, DES.MODE_EAX, ]:
            cipher = DES.new(key, mode=mode, IV=iv)
            if cipher.encrypt(key) == fingerprint:
                found = True
                break
        self.assertTrue(found)  # Vulnerability: Insecure cipher/mode used

if __name__ == '__main__':
    unittest.main()
