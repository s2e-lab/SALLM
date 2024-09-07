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

    if root == None:
        return
    else:
        value = computeTree(root.left)
        if root.val == '^':
            rightVal = computeTree(root.right.right)
            value = sqrt(rightVal)
        if root.val == '*':
            rightVal = computeTree(root.right.right)
            value = value*root.right.right
        if root.val == '/':
            rightVal = computeTree(root.right.right)
            value = value / root