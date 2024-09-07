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

    stack = []
    stack.append(root<mask_1> right = stack.pop()
        elif root.val == '-' and len(stack) > 0:  # pop two numbers and find the substraction of them
            right = stack.pop()
            left = stack.pop()
            root.left = TreeNode(int(right.val) - int(left.val))
            cur = TreeNode('-')
            cur.left = left
            cur.right = right
            root = cur
            stack.append(root)
       