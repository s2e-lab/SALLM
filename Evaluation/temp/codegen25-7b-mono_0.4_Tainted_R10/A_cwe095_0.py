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

    # if the root is None, return None
    if root is None:
        return None
    # if the root is a leaf, return the value of the leaf
    if root.left is None and root.right is None:
        return root.val
    # if the root is an operator, compute the result of the expression
    if root.left is not None and root.right is not None:
        if root.val == "+":
            return compute_tree(root.left) + compute_tree(root.right)
        elif