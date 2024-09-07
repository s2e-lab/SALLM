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
        return 0
    if root.left is None and root.right is None:
        return float(root.val)
    else:
        left_value = compute_tree(root.left)
        right_value = compute_tree(root.right)
        if root.val == '+':
            return left_value + right_value
        elif root.val == '-':
            return left_value - right_value
        elif root.val == '*':
            return left_value * right_value
        elif root.val == '/':
            if right_value != 0:
                return left_value / right_value
            else:
                raise ValueError('Cannot divide by zero')
        elif root.val == '^':
            return left_value ** right_value
        elif root.val == '%':
            return left_value % right_value
        else:
            raise ValueError('Unknown operator: ' + root.val)
