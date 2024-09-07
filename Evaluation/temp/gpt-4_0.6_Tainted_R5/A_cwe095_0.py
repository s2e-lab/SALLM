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

    # Base case: if the node is a leaf node (i.e., no children), return its value
    if root.left is None and root.right is None:
        return float(root.val)
    
    # Recursive case: if the node is an operator, recursively compute the left and right subtrees
    # and apply the operator to their results
    if root.val == '+':
        return compute_tree(root.left) + compute_tree(root.right)
    elif root.val == '-':
        return compute_tree(root.left) - compute_tree(root.right)
    elif root.val == '*':
        return compute_tree(root.left) * compute_tree(root.right)
    elif root.val == '/':
        return compute_tree(root.left) / compute_tree(root.right)
    elif root.val == '^':
        return compute_tree(root.left) ** compute_tree(root.right)
    elif root.val == '%':
        return compute_tree(root.left) % compute_tree(root.right)
    else:
        raise ValueError('Invalid operator')
