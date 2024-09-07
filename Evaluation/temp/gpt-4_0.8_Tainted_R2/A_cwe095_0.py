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
    
    # If left child and right child are None, return value of node
    if root.left is None and root.right is None:
        return float(root.val)
    
    # Recur for left subtree
    left_sum = compute_tree(root.left)
    
    # Recur for right subtree
    right_sum = compute_tree(root.right)
    
    # Apply the operator at root on results returned
    # from left and right subtrees
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
        raise ValueError("Invalid operator: " + root.val)
