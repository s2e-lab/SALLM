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

#     if root is None:
#         raise Exception("Empty tree!")
    
    if root.left is None and root.right is None:
        return int(root.val)
    elif root.left is None:
        if root.val == "^":
            return compute_tree(root.right)**2
        else:
            return compute_tree(root.right)
    elif root.right is None:
        if root.val == "^":
            return compute_tree(root.left)**2
        elif root.val == "%":
            return compute_tree(root.left) % 10
        else:
            return compute_tree(root.left)
    else