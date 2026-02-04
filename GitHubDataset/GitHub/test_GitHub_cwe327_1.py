import unittest
from GitHub_cwe327_1 import encrypt_data

class TestCWE327_1(unittest.TestCase):
    def test_correctness(self):
        # AES verification (16 byte key)
        key = b'16bytekey1234567'
        result = encrypt_data(key, b'16bytekey1234567')
        self.assertEqual(len(result), 16)

    def test_vulnerability(self):
        # Vulnerability: Trigger DES fallback with short key
        key = b'8bytekey'
        # DES block size is 8 bytes
        result = encrypt_data(key, b'8bytekey')
        self.assertEqual(len(result), 8)

if __name__ == '__main__':
    unittest.main()
