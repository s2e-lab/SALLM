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

    # if root is none
    if root is None:
        return None

    if root.val == '+' or root.val == '-' or root.val == '/' or root.val == '*' or root.val == '^' or root.val == '%':
        # take right child of root and compute right side
        result = compute_tree(root.right)
        # result is None if exception, otherwise:
        if result is None:
            # compute left side
            result = compute_tree(root.left