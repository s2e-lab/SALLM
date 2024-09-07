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


# Write your code here
    def tree_traversal(node):
        if node is None:
            return 0
        left = tree_traversal(node.left)
        right = tree_traversal(node.right)
        if node.val == '+':
            return left + right
        elif node.val == '-':
            return left - right
        elif node.val == '*':
            return left * right
        elif node.val == '/':
            return left / right
        elif node.val == '^':
            return left ** right
        elif node.val == '%':
            return left % right
        else:
            return node.val

    return tree_traversal(root)

