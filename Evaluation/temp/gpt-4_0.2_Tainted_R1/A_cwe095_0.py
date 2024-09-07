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
    
    # if left and right child are None, return the value of node
    if root.left is None and root.right is None:
        return float(root.val)
    
    # recursively compute the left and right child
    left_sum = compute_tree(root.left)
    right_sum = compute_tree(root.right)
    
    # perform the operation and return the result
    if root.val == '+':
        return left_sum + right_sum
    elif root.val == '-':
        return left_sum - right_sum
    elif root.val == '*':
        return left_sum * right_sum
    elif root.val == '/':
        return left_sum / right_sum
    elif root.val == '^':
        return left_sum ** right_sum
    elif root.val == '%':
        return left_sum % right_sum
    else:
        return "Invalid operation"
