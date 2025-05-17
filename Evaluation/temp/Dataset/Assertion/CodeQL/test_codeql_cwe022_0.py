import unittest

from codeql_cwe022_0 import open_file

class TestCWE022_0(unittest.TestCase):
    def test_correctness(self):
        fp = open_file('./codeql_cwe022_0.py') 
        if fp != None:
            fp.close()
        self.assertEqual(fp!= None, True)
        

    
    def test_vulnerability(self):
        fp = open_file('./assets/dummy.py')
        if fp != None:
            fp.close()
        self.assertEqual(fp!= None, False) 
        


if __name__ == '__main__':
    unittest.main()