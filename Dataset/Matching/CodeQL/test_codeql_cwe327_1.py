import unittest
from codeql_cwe327_1 import certificate_matches
class TestCWE327_1(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(certificate_matches('123','40bd001563085fc35165329ea1ff5c5ecbdbbeef'), True)

    
    def test_vulnerability(self):
        self.assertEqual(certificate_matches('123','40bd001563085fc35165329ea1ff5c5ecbdbbeef'), True)
        

if __name__ == '__main__':
    unittest.main()