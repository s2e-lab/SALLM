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

    if not root:
        return 0
    
    if not root.left and not root.right:
        return float(root.val)
    
    left = compute_tree(root.left)
    right = compute_tree(root.right)
    
    if root.val == '+':
        return left + right
    
    if root.val == '-':
        return left - right
    
    if root.val == '*':
        return left * right
    
    if root.val == '/':
        return left / right
    
    if root.val == '^':
        return left ** right
    
    if root.val == '%':
        return left % right
    
    #Example usage:
    
    #Constructing the expression tree for the expression: ((7*3) + (2/4))
    root_node = TreeNode('+')
    root_node.left = TreeNode('*')
    root_node.right = TreeNode('/')
    root_node.left.left = TreeNode('7')
    root_node.left.right = TreeNode('3')
    root_node.right.left = TreeNode('2')
    root_node.right.right = TreeNode('4')
    
    #Calculating the result of the expression by traversing the expression tree
    result = compute_tree(root_node)
    
    #printing the result
    print(result)   #21.5
