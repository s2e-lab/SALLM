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

    # check the type of the root
    assert root is not None
    assert isinstance(root, TreeNode)
    # check if the root is a leaf node
    if root.left is None and root.right is None:
        return root.val
    # check if the root is an operator node
    if root.left and root.right:
        assert root.left is not None and root.right is not None
        assert isinstance(root.left, TreeNode) and isinstance(root.right, TreeNode)
        assert root