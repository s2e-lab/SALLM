import unittest


class TestExample(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(1, 1)

    def test_fail(self):
        self.assertEqual(1, 2)

    def test_error(self):
        x = 1/0 # division by zero error
        self.assertTrue(True)

