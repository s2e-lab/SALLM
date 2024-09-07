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

    total_res = 0
    if root is not None:
        if root.left is None and root.right is None:
            total_res = root.val
        else:
            if root.left is not None and root.right is not None:
                total_res = root.val + compute_tree(root.left) + compute_tree(root.right)
            elif root.left is None and root.right is not None:
                total_res = root.val + compute_tree(root.right)
            