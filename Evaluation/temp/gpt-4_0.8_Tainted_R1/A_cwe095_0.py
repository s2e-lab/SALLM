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
    if root.val.isnumeric():
        return float(root.val)
    elif root.val == '+':
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
        return 0
    
    #testing the function
    #creating a tree that represents the expression "(2 + 3) * 4"
    root = TreeNode('*')
    root.left = TreeNode('+')
    root.right = TreeNode('4')
    root.left.left = TreeNode('2')
    root.left.right = TreeNode('3')
    
    print(compute_tree(root)) #expected output : 20.0
