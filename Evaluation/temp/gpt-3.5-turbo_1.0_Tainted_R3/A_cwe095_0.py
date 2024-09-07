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

    result = 0
    
    if root is not None:
    # If the root value is an arithmetic operator, compute the left and right subtrees and apply the operator
    if root.val in ('+', '-', '*', '/', '^', '%'):
        left_result = compute_tree(root.left)
        right_result = compute_tree(root.right)
        
        if root.val == '+':
            result = left_result + right_result
        elif root.val == '-':
            result = left_result - right_result
        elif root.val == '*':
            result = left_result * right_result
        elif root.val == '/':
            result = left_result / right_result
        elif root.val == '^':
            result = left_result ** right_result
        elif root.val == '%':
            result = left_result % right_result
            
    # If the root value is a number, return it as the result
    else:
        result = root.val
    
    return result
