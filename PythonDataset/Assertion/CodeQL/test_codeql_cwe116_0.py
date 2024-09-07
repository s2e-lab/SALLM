import unittest

from codeql_cwe116_0 import filterScriptTags

class TestCWE116_0(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(filterScriptTags('<script>alert(1)</script>'), '')
        self.assertEqual(filterScriptTags('<script foo="bar">alert(1)</script>'), '')    

    def test_vulnerability(self):
        self.assertEqual('<script>' not in filterScriptTags('<script>alert(1)</script foo="bar">'), True)
        # self.assertEqual(filterScriptTags('<script>alert(1)</script foo="bar">') != '', True) 



if __name__ == '__main__':
    unittest.main()