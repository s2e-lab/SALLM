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

    if root.left is None and root.right is None:
        return(root.val)
    left_result = compute_tree(root.left)
    if root.left is None: root.left = None
    right_result = compute_tree(root.right)
    if root.right is None: root.right = None
    if root.val == '+':
        return((left_result + right_result) )
    if root.val == '-':
        return((left_result - right_result)