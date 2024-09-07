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

    # approach:
    - if the root is None, return 0
    - if the root does not have any left or right child, convert the value to float and return
    - else, recursively compute the left and right subtrees
    - compute the result based on the operator at the root and the values of the left and right subtrees
    - return the result
    
    
    def compute_tree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return float(root.val)
    left_val = compute_tree(root.left)
    right_val = compute_tree(root.right)
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
