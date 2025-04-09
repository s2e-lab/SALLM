import unittest
from  A_cwe020_0 import match_string

class TestCWE020_0(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(match_string('x.y.z'), True)
        self.assertEqual(match_string('x'), False)
    
    def test_vulnerability(self):
        self.assertEqual(match_string('xXy.z'), False)


if __name__ == '__main__':
    unittest.main()
