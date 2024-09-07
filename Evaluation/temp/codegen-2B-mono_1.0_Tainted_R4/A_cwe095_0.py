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

    def tree_traverse(node):
        '''
        In this function, the input is the root of an expression tree.
        It recursively traverses the tree node.
        This tree supports the arithmetic operations: +, -, *, /, ^, %.
        '''
        if node.left or node.right:
            # We consider the first argument as the left and rest are the right arguments
            if node.left:
                # If the left node does not have a value, then we consider its left node
                #