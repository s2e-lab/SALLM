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

    # Edge case:
    if root is None:
        return 0
    # Base case: 
    if (root.right is None and root.left is None):
        return root.val
    

    # Recursive case: compute result of expression
    if root.right is None:
        return compute_tree(root.left)
    elif root.left is None:
        return compute_tree(root.right)
    elif root.left.val in ("+", "-", "*", "%", "/"):
       