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

    # To compute the mathematical expression stored in the expression tree, we can use a recursive approach.
    # We traverse the tree in a depth-first manner, starting from the root node.
    # At each node, we check the value of the node.
    # If the value is a number, we return the value.
    # If the value is an operator, we recursively compute the values of the left and right subtrees and perform the corresponding operation.
    # Once we have computed the values of the left and right subtrees, we perform the operation and return the result.
    
    # Here is the code to implement this approach:
    
    def compute_tree(root):
    # Base case: if the root is None, return 0
    if root is None:
        return 0
    
    # If the root is a number, return its value
    if root.val.isdigit():
        return float(root.val)
    
    # Compute the values of the left and right subtrees
    left_val = compute_tree(root.left)
    right_val = compute_tree(root.right)
    
    # Perform the operation based on the operator
    if root.val == '+':
        return left_val + right_val
    elif root.val == '-':
        return left_val - right_val
    elif root.val == '*':
        return left_val * right_val
    elif root.val == '/':
        return left_val / right_val
    elif root.val == '^':
        return left_val ** right_val
    elif root.val == '%':
        return left_val % right_val
