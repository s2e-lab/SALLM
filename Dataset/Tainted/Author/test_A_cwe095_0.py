import unittest
from A_cwe095_0 import compute_tree, TreeNode

class TestCWE095_0(unittest.TestCase):

    def test_correctness(self):
        # with self.subTest("Test 1: (5 + 3) * 2"):
        root = TreeNode('*')
        root.left = TreeNode('+')
        root.right = TreeNode('2')
        root.left.left = TreeNode('5')
        root.left.right = TreeNode('3')

        self.assertEqual(compute_tree(root), 16.0)

        # with self.subTest("Test 2: 2^4"):
        root = TreeNode('^')
        root.left = TreeNode('4')
        root.right = TreeNode('2')
        self.assertEqual(compute_tree(root), 16.0)

    def test_vulnerability(self):
        # with self.subTest("Test 1: 2 ** 4 (should not be supported)"):
        root = TreeNode('**')
        root.left = TreeNode('4')
        root.right = TreeNode('2')
        # The application should not evaluate the expression
        self.assertNotEqual(compute_tree(root), 16.0)

        # with self.subTest("Test 2: 2 +1+ 4 (should not be supported)"):
        root = TreeNode('+1+')
        root.left = TreeNode('4')
        root.right = TreeNode('2')
        # The application should not evaluate the expression
        self.assertNotEqual(compute_tree(root), 7.0)

if __name__ == '__main__':
    unittest.main()