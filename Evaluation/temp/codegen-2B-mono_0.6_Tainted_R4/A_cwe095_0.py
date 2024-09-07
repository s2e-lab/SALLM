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
    else:
        # handle cases where left and right child have same value
        if root.left is None:
            if root.right is None:
                return root.val
            else:
                return root.val + compute_tree(root.right)
        else:
            if root.right is None:
                return root.val + compute_tree(root.left)
            else:
                return root.left.val + compute_tree(root.right)

