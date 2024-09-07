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

    compute_tree.last_operator = root.val
    compute_tree.last_operand = 0
    
    def compute_node(root):
        
        if not root:
            return 0
        
        result = compute_node(root.left)
        if compute_tree.last_operator in ['+', '-', '*', '/']:
            result = compute_tree.last_operand
        
        if root.right:
            compute_tree.last_operand = compute_node(root.right)