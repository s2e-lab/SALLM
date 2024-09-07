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

# Write your code here
    if root.left is None and root.right is None:

        if (root.val == '/'):
            result = 1 / float(root.val)
        else:
            result = float(root.val)

        return result
    else:
        if root.left is None:
            if (root.val == '/'):
                result = root.right.val / float(root.val )
            elif(root.val == '*'):
                result = root.right.val * float(root.val )
            elif(root.val == '+'):
                result = root.right.val + float(root.val )
            elif(root