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

# ---------------------------------------------------
#  This is a wrong answer.
# ---------------------------------------------------
#    res = 0.0
#    op = '+'
#    stack = list()
#    node = root
#    while node is not None or len(stack) > 0:
#        if node is not None:
#            stack.append(node.val)
#            node = node.left
#        else:
#            node = stack.pop()
#            if node == '+':
#                res += stack.pop()
#            elif node == '-':
#                res -= stack.pop()
#            elif node