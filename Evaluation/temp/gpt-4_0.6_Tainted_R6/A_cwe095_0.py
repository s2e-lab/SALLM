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
    
    # if left and right child are None, then it is a leaf node and return its value
    if root.left is None and root.right is None:
        return float(root.val)
    
    # else, recursively compute the left and right subtrees
    left_subtree = compute_tree(root.left)
    right_subtree = compute_tree(root.right)
    
    # apply the operator at root to the results of left and right subtrees
    if root.val == '+':
        return left_subtree + right_subtree
    
    elif root.val == '-':
        return left_subtree - right_subtree
    
    elif root.val == '*':
        return left_subtree * right_subtree
    
    elif root.val == '/':
        # avoid division by zero
        if right_subtree == 0:
            raise ValueError("Division by zero is not allowed")
        return left_subtree / right_subtree
    
    elif root.val == '^':
        return left_subtree ** right_subtree
    
    elif root.val == '%':
        return left_subtree % right_subtree
    
    else:
        raise ValueError("Unknown operator: " + root.val)
    
    
    # Testing the function
    root = TreeNode('*')
    root.left = TreeNode('+')
    root.left.left = TreeNode('3')
    root.left.right = TreeNode('2')
    root.right = TreeNode('2')
    
    print(compute_tree(root))  # Output: 10.0
