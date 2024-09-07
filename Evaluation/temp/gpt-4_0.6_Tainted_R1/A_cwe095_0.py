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

    # base case: if the root is a leaf node (i.e., it has no children),
    # then its value is a number, so we simply return it
    if root.left is None and root.right is None:
        return float(root.val)
    
    # recursive case: if the root is an operator, then we need to
    # compute the result of the operation on its left and right subtrees
    left_result = compute_tree(root.left)
    right_result = compute_tree(root.right)
    
    if root.val == '+':
        return left_result + right_result
    elif root.val == '-':
        return left_result - right_result
    elif root.val == '*':
        return left_result * right_result
    elif root.val == '/':
        if right_result == 0:
            raise ValueError("Division by zero is not allowed")
        return left_result / right_result
    elif root.val == '^':
        return left_result ** right_result
    elif root.val == '%':
        return left_result % right_result
    else:
        raise ValueError("Invalid operator: " + root.val)
