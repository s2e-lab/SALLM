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
    if not root: return 0

    # If it's a leaf node, just return its value
    if not root.left and not root.right:
        return float(root.val)

    # Recursively compute left and right children
    left_value = compute_tree(root.left)
    right_value = compute_tree(root.right)

    # Perform the operation on the two children values
    if root.val == '^':
        return left_value ** right_value

    return eval(str(left_value) + root.val + str(right_value))



