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
    
    # if the node is a leaf (has no children), it means it's a number
    if root.left is None and root.right is None:
        return float(root.val)
    
    # compute the left and right subtrees
    left_subtree = compute_tree(root.left)
    right_subtree = compute_tree(root.right)
    
    # apply the operation of the current node to the results of the left and right subtrees
    if root.val == '+':
        return left_subtree + right_subtree
    elif root.val == '-':
        return left_subtree - right_subtree
    elif root.val == '*':
        return left_subtree * right_subtree
    elif root.val == '/':
        return left_subtree / right_subtree
    elif root.val == '^':
        return left_subtree ** right_subtree
    elif root.val == '%':
        return left_subtree % right_subtree
    else:
        raise ValueError('Invalid operator')
