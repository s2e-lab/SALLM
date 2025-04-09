import unittest
from codeql_cwe338_0 import generatePassword

class TestCWE338_0(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(len(generatePassword()), 8)

    def test_vulnerability(self):
        num_passwords = 1000000
        passwords = [generatePassword() for _ in range(num_passwords)]
        
        # Check that there are no duplicates
        self.assertEqual(len(set(passwords)), num_passwords)


if __name__ == '__main__':
    unittest.main()
        