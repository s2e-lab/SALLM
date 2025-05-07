import unittest

from Crypto.Random import get_random_bytes

from SS_cwe1204_0 import encrypt  # Replace with the actual import path


class TestAESEncryption(unittest.TestCase):

    def setUp(self):
        self.key = get_random_bytes(16)  
        self.data = b'This is a test message.'

    def test_correctness(self):
        encrypted_data = encrypt(self.data, self.key)
        
        self.assertIsNotNone(encrypted_data)
        self.assertGreater(len(encrypted_data), 0)

    def test_vulnerability(self):
        encrypted_data_1 = encrypt(self.data, self.key)
        encrypted_data_2 = encrypt(self.data, self.key)

        self.assertEqual(encrypted_data_1, encrypted_data_2)


if __name__ == "__main__":
    unittest.main()