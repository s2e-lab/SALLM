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


# --------------------------------------------------------------
# # Pseudocode
# 1. Base Case
#       - if the node is None then return 0.0
#       - if we've reached the end of a left subtree
#           - traverse right subtree and multiply by exponent
#       - if we've reached a right subtree
#       - traverse left subtree and divide
#       - if we've reached the end and left subtree is None then
#           - return the integer value * 1.0
# 

#         *1.1
#             - traverse from the left subtree and compute the root*number
#             - traverse from the right subtree and compute