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
        return None

    if root.left is None and root.right is None:
        return root.val

    if root.left is None:
        return root.val + compute_tree(root.right)

    if root.right is None:
        return compute_tree(root.left) + root.val

    return compute_tree(root.left) + compute_tree(root.right) + root.val

