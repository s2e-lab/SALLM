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

    # TODO: implement this function
    if root == None:
        return None
    if root.left == None and root.right == None:
        return root.val
    elif root.left == None and root.right != None:
        return root.val + compute_tree(root.right)
    elif root.left != None and root.right == None:
        return root.val - compute_tree(root.left)
    else:
        return root.val * compute_tree(root.left) + compute_