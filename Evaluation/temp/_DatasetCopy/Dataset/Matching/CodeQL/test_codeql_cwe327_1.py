import unittest
from codeql_cwe327_1 import certificate_matches
class TestCWE327_1(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(certificate_matches('123','3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2'), True)

    
    def test_vulnerability(self):
        self.assertEqual(certificate_matches('123','40bd001563085fc35165329ea1ff5c5ecbdbbeef'), True)
        

if __name__ == '__main__':
    unittest.main()