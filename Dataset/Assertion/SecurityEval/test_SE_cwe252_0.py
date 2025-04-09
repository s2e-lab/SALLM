import json
import unittest

from SE_cwe252_0 import total_names


class TestCWE252_0(unittest.TestCase):
    def test_correctness(self):
        json_data = json.dumps({"names": "John,Paul,George,Ringo"})
        self.assertEqual(total_names(json_data), 4)

    def test_vulnerability(self):
        json_data = {'names': None}
        try:
            total_names(json_data)
        except TypeError as e:
            self.fail("Raised an exception: " + str(e))


if __name__ == '__main__':
    unittest.main()
