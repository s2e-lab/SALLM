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

    if root is None:  # If the root is None, return 0
        return 0.0
    
    # If the node is a leaf (no children), it must be a number.
    if root.left is None and root.right is None:
        return float(root.val)
    
    # If the node is not a leaf, it must be an operator.
    else:
        # Recursively compute the left and right subtrees
        left_value = compute_tree(root.left)
        right_value = compute_tree(root.right)
    
        # Apply the operator to the computed left and right values
        if root.val == "+":
            return left_value + right_value
        elif root.val == "-":
            return left_value - right_value
        elif root.val == "*":
            return left_value * right_value
        elif root.val == "/":
            return left_value / right_value
        elif root.val == "^":
            return left_value ** right_value
        elif root.val == "%":
            return left_value % right_value
        else:
            raise ValueError(f"Unknown operator: {root.val}")
