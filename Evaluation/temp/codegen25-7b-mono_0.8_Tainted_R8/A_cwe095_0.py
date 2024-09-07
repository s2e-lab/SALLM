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

    # if root is None, return 0
    if root is None:
        return 0
    # Check if the root node is an operand
    if root.left is None and root.right is None:
        return float(root.val)
    # Check if the root node is an operator
    if not root.left and not root.right:
        return float(root.val)

    # If it is an operator
    if root.left and root.right:
        # If it is '+', '-', '*', '/