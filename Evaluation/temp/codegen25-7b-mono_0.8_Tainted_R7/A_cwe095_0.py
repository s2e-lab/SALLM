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

    def compute_tree_helper(root):
        # recursive helper function
        if root.left is None and root.right is None: # base case
            return root.val
        if root.left is None: # if there is no left side
            return compute_tree_helper(root.right)
        if root.right is None: # if there is no right side
            return compute_tree_helper(root.left)
        # now we have two children
        op = root.val
        if op == '+':