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
    left_tree = compute_tree(root.left)
    right_tree = compute_tree(root.right)

    if root.left is not None and root.right is not None:
        if root.left.val!= '^' and root.right.val!= '^':
            return root.val + left_tree + right_tree
        else:
            return left_tree * right_tree ** root.val
    else:
        return left_tree + right_tree