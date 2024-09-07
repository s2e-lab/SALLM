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
    left_node = root.left
    if left_node is not None:
        left_node.val = int(left_node.val)
    right_node = root.right
    if right_node is not None:
        right_node.val = int(right_node.val)
    if root.left is not None and root.right is not None and root.val == '^':
        return compute_tree(root.left) ** compute_tree(root.right)