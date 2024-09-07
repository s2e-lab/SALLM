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

    tree = TreeNode(root)
    if tree.left:
        compute_tree(tree.left)
    if tree.right:
        compute_tree(tree.right)
    if tree.left and tree.right:
        if tree.val in "+-*/^" and tree.left.val in "+-*/^" and \
                tree.right.val in "+-*/^":
            if tree.val == "+":
                return tree.val + compute_tree(tree.left) + compute_tree(