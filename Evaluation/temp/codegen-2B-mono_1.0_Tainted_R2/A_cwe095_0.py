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

    result = 0

    if root is None:
        return False

    if root.left is None and root.right is None:
        return root.val

    if root.left.val == '+':
        left_num = root.left.left.val + root.left.right.val
        right_num = root.right.left.val + root.right.right.val
        result = left_num + root.val + right_num

        right_tree = compute_tree(root.right)

        left_