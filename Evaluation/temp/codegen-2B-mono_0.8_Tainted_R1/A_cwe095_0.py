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

    if root.left is None and root.right is None:
        if root.val == '+':
            return 1
        elif root.val == '-':
            return 0
        elif root.val == '*':
            return 1
        elif root.val == '/':
            return 0.5
        elif root.val == '^':
            return root.left.val * root.left.val
        elif root.val == '%':
            return root.left.val / root.right.