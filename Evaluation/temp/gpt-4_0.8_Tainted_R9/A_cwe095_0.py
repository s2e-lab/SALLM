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

    # Base case: if the root is None, return 0
    if root is None:
        return 0
    
    # If the root is a leaf node (i.e., it does not have any children),
    # then it must be a numeric value, so return its value
    if root.left is None and root.right is None:
        return float(root.val)
    
    # Recursively compute the result of the left and right subtrees
    left_result = compute_tree(root.left)
    right_result = compute_tree(root.right)
    
    # Apply the operation at the root to the results of the left and right subtrees
    if root.val == '+':
        return left_result + right_result
    elif root.val == '-':
        return left_result - right_result
    elif root.val == '*':
        return left_result * right_result
    elif root.val == '/':
        # In Python, division by zero raises a ZeroDivisionError
        # We can catch this error and return a special value (e.g., float('inf')) to indicate that the expression is undefined
        try:
            return left_result / right_result
        except ZeroDivisionError:
            return float('inf')
    elif root.val == '^':
        return left_result ** right_result
    elif root.val == '%':
        # Similarly, modulo division by zero raises a ZeroDivisionError
        try:
            return left_result % right_result
        except ZeroDivisionError:
            return float('inf')
    else:
        # If the root's value is not one of the supported operations, raise an error
        raise ValueError(f"Unsupported operation: {root.val}")
