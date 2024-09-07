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

    # base case: if the node is a leaf (it has no children), it is a number
    if root.left is None and root.right is None:
        return float(root.val)
    
    # recursive case: if the node is not a leaf, it is an operator
    else:
        if root.val == '+':
            return compute_tree(root.left) + compute_tree(root.right)
        elif root.val == '-':
            return compute_tree(root.left) - compute_tree(root.right)
        elif root.val == '*':
            return compute_tree(root.left) * compute_tree(root.right)
        elif root.val == '/':
            return compute_tree(root.left) / compute_tree(root.right)
        elif root.val == '^':
            return compute_tree(root.left) ** compute_tree(root.right)
        elif root.val == '%':
            return compute_tree(root.left) % compute_tree(root.right)
        else:
            raise ValueError('Unknown operator: ' + root.val)
