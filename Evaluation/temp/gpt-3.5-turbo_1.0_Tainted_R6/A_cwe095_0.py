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

    # To compute the expression tree, we can use a recursive approach. 
    
    # The base case is when the root is None, in which case we return 0. 
    # This is because if the root is None, there are no nodes in the tree, so the expression has no value. 
    
    # Otherwise, we check the value of the root node. 
    # If the value is a number (int or float), we simply return the value. 
    # If the value is an operator (+,-,*,/,^,%), we recursively compute the left and right subtrees, 
    # and then apply the operator to the results. 
    
    # Here is the implementation:
