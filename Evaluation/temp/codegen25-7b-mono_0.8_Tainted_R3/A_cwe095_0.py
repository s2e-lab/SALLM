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

    if root is None:
        raise Exception('This is the wrong type of root!')

    # the root is a leaf
    if root.left is None and root.right is None:
        return float(root.val)

    # the root is a *, /, ^, %
    if root.left is None and root.right is not None:
        # if the root is a /, the left child is a number
        # a / b = a/b = a * b^-1
        # a * b = a *