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
    
    # if the node is a leaf (has no children), then it's a number and we return its value
    if root.left is None and root.right is None:
        return float(root.val)
    
    # otherwise, we compute the left and right subtrees
    left = compute_tree(root.left)
    right = compute_tree(root.right)
    
    # and we perform the operation at the current node
    if root.val == '+':
        return left + right
    elif root.val == '-':
        return left - right
    elif root.val == '*':
        return left * right
    elif root.val == '/':
        return left / right
    elif root.val == '^':
        return left ** right
    elif root.val == '%':
        return left % right
    else:
        raise ValueError('Unknown operator: ' + root.val)
