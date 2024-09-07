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

    values = []
    pre_order_traversal(root, values)
    summ = values[0]
    for i in range(1, len(values))[::-1]:
        if values[i - 1] == '+':
            summ += values[i]
        elif values[i - 1] == '-':
            summ -= values[i]
        elif values[i-1] == '*':
            summ *= values[i]
        elif values[i-1