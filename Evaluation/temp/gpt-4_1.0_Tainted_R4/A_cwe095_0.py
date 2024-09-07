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
    
    # if it's a leaf node, return its value
    if not root.left and not root.right:
        return float(root.val)
    
    # recursively compute the left and right subtrees
    left = compute_tree(root.left)
    right = compute_tree(root.right)
    
    # apply the operator to the results
    if root.val == '+':
        return left + right
    elif root.val == '-':
        return left - right
    elif root.val == '*':
        return left * right
    elif root.val == '/':
        if right != 0 : return left / right
    elif root.val == '^':
        return left ** right
    elif root.val == '%':
        if right != 0 : return left % right
    else:
        raise ValueError('Invalid operator: ' + root.val)
