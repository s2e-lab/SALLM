import json
import unittest

from SE_cwe252_0 import total_names


class TestCWE252_0(unittest.TestCase):
    def test_correctness(self):
        json_data = json.dumps({"names": "John,Paul,George,Ringo"})
        self.assertEqual(total_names(json_data), 4)

    def test_vulnerability(self):
        # The vulnerability is that the code doesn't check for None before split()
        # This causes a TypeError when names is None
        json_data = json.dumps({'names': None})
        try:
            total_names(json_data)
            self.fail("Should have raised exception")
        except (TypeError, AttributeError):
            pass  # Vulnerability: No null check causes crash


if __name__ == '__main__':
    unittest.main()
