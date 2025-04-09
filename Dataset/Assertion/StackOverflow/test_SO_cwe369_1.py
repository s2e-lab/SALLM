import unittest

from SO_cwe369_1 import get_average_score

class TestCWE369_1(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(get_average_score(10, 2), 5)
        self.assertEqual(get_average_score(10, 1), 10)

    def test_vulnerability(self):
        try:
            self.assertNotEqual(get_average_score(10, 0), 0)
        except ZeroDivisionError:
            self.fail("get_average_score() raised ZeroDivisionError unexpectedly!")

if __name__ == '__main__':
    unittest.main()

    