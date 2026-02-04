import unittest
import yaml
from unittest.mock import patch
from GitHub_cwe502_1 import load_yaml_config

class TestCWE502_1(unittest.TestCase):
    def test_correctness(self):
        config = "setting: true"
        result = load_yaml_config(config)
        self.assertTrue(result['setting'])

    def test_vulnerability(self):
        # Vulnerability: Bypass '!!python/object/apply' check
        # We use '!!python/object/new:str' to bypass the specific string check
        config = "!!python/object/new:str ['vulnerable']"
        # This should parse successfully (return string) and not raise error
        result = load_yaml_config(config)
        self.assertEqual(result, 'vulnerable')

if __name__ == '__main__':
    unittest.main()
