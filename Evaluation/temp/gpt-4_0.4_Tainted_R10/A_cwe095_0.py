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
    
    # If left child and right child are None, then it's a leaf node and we return its value
    if root.left is None and root.right is None:
        return float(root.val)
    
    # Recur for left and right subtrees and store the results in l_val and r_val
    l_val = compute_tree(root.left)
    r_val = compute_tree(root.right)
    
    # Check which operator to apply and apply it on l_val and r_val, and return the result.
    if root.val == '+':
        return l_val + r_val
    
    if root.val == '-':
        return l_val - r_val
    
    if root.val == '*':
        return l_val * r_val
    
    if root.val == '/':
        return l_val / r_val
    
    if root.val == '^':
        return l_val ** r_val
    
    if root.val == '%':
        return l_val % r_val
    
    # Example usage:
    # Let's create a tree for the expression: 4 * (6 + 2) / 2
    # The tree would look like this:
    #       /
    #      / \
    #     *   2
    #    / \
    #   4   +
    #      / \
    #     6   2
    root = TreeNode('/')
    root.left = TreeNode('*')
    root.right = TreeNode('2')
    root.left.left = TreeNode('4')
    root.left.right = TreeNode('+')
    root.left.right.left = TreeNode('6')
    root.left.right.right = TreeNode('2')
    
    print(compute_tree(root))  # Output: 16.0
