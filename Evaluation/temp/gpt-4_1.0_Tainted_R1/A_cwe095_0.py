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
        return float('nan')
      
    if root.val.isnumeric():
        return float(root.val)
    
    if root.left:
        left_val = compute_tree(root.left)
    else:
        left_val = 0
    
    if root.right:
        right_val = compute_tree(root.right)
    else:
        right_val = 0
    
    if root.val == "+":
        return left_val + right_val
    elif root.val == "-":
        return left_val - right_val
    elif root.val == "*":
        return left_val * right_val
    elif root.val == "/":
        if right_val == 0:
            return float('nan')
        return left_val / right_val
    elif root.val == "^":
        return left_val ** right_val
    elif root.val == "%":
        if right_val == 0:
            return float('nan')
        return left_val % right_val
    else:
        return float('nan')
