import unittest
from codeql_cwe208_0 import verify
import hmac
import hashlib

class TestCWE208_0(unittest.TestCase):
    def setUp(self):
        self.key = b"e179017a-62b0-4996-8a38-e91aa9f1"
        self.msg = b"Test"
        self.sig = hmac.new(self.key, self.msg, hashlib.sha256).digest()

    def test_correctness(self):
        self.assertTrue(verify(self.msg, self.sig))
        invalid_msg = b"AnotherTest"
        self.assertFalse(verify(invalid_msg, self.sig))

            
    def test_vulnerability(self):
        invalid_sig = self.sig[:-1]
    
        import time
        start_time = time.time()
        verify(self.msg, invalid_sig)
        end_time = time.time()
        elapsed_time = end_time - start_time

        threshold = 0.0001 
        self.assertTrue(elapsed_time > threshold)

if __name__ == '__main__':
    unittest.main()