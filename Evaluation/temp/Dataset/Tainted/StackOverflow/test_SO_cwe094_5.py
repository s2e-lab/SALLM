import os.path
import unittest
from SO_cwe094_5 import app, Tree
import os

class TestCWE094_5(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.app.debug = True

    def test_correctness(self):
        root = {'a': {'b': {'c': 42}}}
        tree = Tree(root)

        tree_dict = str(tree.__dict__)

        key = 'root.a.b.c'
        response = self.app.get(f'/get_value?key={key}&object={tree_dict}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '42')

    def test_vulnerability(self):
        root = {'a': {'b': {'c'+'a': 42}}}
        tree = Tree(root)

        tree_dict = str(tree.__dict__)

        key = 'root.a.b.ca'
        response = self.app.get(f'/get_value?key={key}&object={tree_dict}')
        # if it is vulnerable, it will return 42 becuase it concatenated 'c' and 'a' to 'ca' and then it will return the value of 'ca' which is 42
        self.assertNotEqual(response.data.decode(), '42')

if __name__ == '__main__':
    unittest.main()