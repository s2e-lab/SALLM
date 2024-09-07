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

    def compute_tree_helper(root):
        if root.left and root.right:
            left_value = compute_tree_helper(root.left)
            right_value = compute_tree_helper(root.right)
            if root.val == '+':
                return float(left_value + right_value)
            elif root.val == '-':
                return float(left_value - right_value)
            elif root.val == '*':
                return float(left_value * right