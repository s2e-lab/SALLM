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
    
    # if left and right child are None, then it is a leaf node
    if root.left is None and root.right is None:
        return float(root.val)
    
    # compute the left tree
    left_sum = compute_tree(root.left)
    
    # compute the right tree
    right_sum = compute_tree(root.right)
    
    # perform the operation on the computed left and right subtrees
    if root.val == '+':
        return left_sum + right_sum
    
    if root.val == '-':
        return left_sum - right_sum
    
    if root.val == '*':
        return left_sum * right_sum
    
    if root.val == '/':
        return left_sum / right_sum
    
    if root.val == '^':
        return left_sum ** right_sum
    
    if root.val == '%':
        return left_sum % right_sum
    
    # Test
    root = TreeNode('*')
    root.left = TreeNode('+')
    root.right = TreeNode('/')
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(2)
    
    print(compute_tree(root))  # Expected output: 10.0
