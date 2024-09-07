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

    # To compute the mathematical expression represented by the expression tree, we can use a recursive approach.
    
    # We start by checking if the root node is None. If it is, we return 0 as the result.
    
    # If the root node is not None, we check if it is a leaf node. If it is, we return the value of the leaf node.
    
    # If the root node is not a leaf node, we recursively compute the values of the left and right subtrees.
    
    # Then, we perform the arithmetic operation specified by the root node's value on the values of the left and right subtrees.
    
    # Finally, we return the result of the arithmetic operation.
    
    # Here is the implementation of the compute_tree function:
