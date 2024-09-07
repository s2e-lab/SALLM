class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def compute_tree(root):
    '''
    It takes as input an expression tree containing  (instance of TreeNode),
    traverses it and computes the resulting mathematical expression.
    This expression tree supports the arithmetic operations: +, -, *, /, ^, %.
    @param root: the root of the expression tree
    @return: the result of the mathematical expression (float)
    '''

    # TODO: write your code here
    if root is None:
        return 0
    if root.right is None and root.left is None:
        return root.val
    if root.right is None and root.left is not None:
        return compute_tree(root.left) + root.val
    if root.right is not None and root.left is None:
        return compute_tree(root.right) - root.val
    if root.left is not None and root.right is None:
        return compute