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
    
    # check if the node is a leaf node
    if root.left is None and root.right is None:
        return float(root.val)
    
    # recursively compute the left and right subtree
    left_val = compute_tree(root.left)
    right_val = compute_tree(root.right)
    
    # perform the mathematical operation based on the node's value
    if root.val == '+':
        return left_val + right_val
    elif root.val == '-':
        return left_val - right_val
    elif root.val == '*':
        return left_val * right_val
    elif root.val == '/':
        return left_val / right_val
    elif root.val == '^':
        return left_val ** right_val
    elif root.val == '%':
        return left_val % right_val
