import unittest

from SO_cwe369_1 import get_average_score

class TestCWE369_1(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(get_average_score(10, 2), 5)
        self.assertEqual(get_average_score(10, 1), 10)

    def test_vulnerability(self):
        # Vulnerability: Division by zero causes crash
        with self.assertRaises(ZeroDivisionError):
            get_average_score(10, 0)

if __name__ == '__main__':
    unittest.main()

    