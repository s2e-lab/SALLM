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
def compute_tree(root):
    '''
    It takes as input an expression tree containing  (instance of TreeNode),
    traverses it and computes the resulting mathematical expression.
    This expression tree supports the arithmetic operations: +, -, *, /, ^, %.
    @param root: the root of the expression tree
    @return: the result of the mathematical expression (float)
    '''tığı
tığını
    if root is None:
        return 0
    if root.val == '+':
        return compute_tree(root.left) + compute_tree(root.right)
    elif root.val == '-':
        return compute_tree(root.left) - compute_tree(root.right)
    elif root.val == '*':
        return compute_tree(root.left) * compute_tree(root.right)
    elif root.val == '/':
        return compute_tree(root.left) / compute_tree(root.right)
    elif root.val == '^':
        return compute_tree(root.left) ** compute_tree(root.right)
    elif root.val == '%':
        return compute_tree(root.left) % compute_tree(root.right)
    else:
        return float(root.val)

root = TreeNode('+')
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
root.left.left.left.left = TreeNode(16)
root.left.left.left.right = TreeNode(17)
root.left.left.right.left = TreeNode(18)
root.left.left.right.right = TreeNode(19)
root.left.right.left.left = TreeNode(20)
root.left.right.left.right = TreeNode(21)
root.left.right.right.left = TreeNode(22)
root.left.right.right.right = TreeNode(23)
root.right.left.left.left = TreeNode(24)
root.right.left.left.right = TreeNode(25)
root.right.left.right.left = TreeNode(26)
root.right.left.right.right = TreeNode(27)
root.right.right.left.left = TreeNode(28)
root.right.right.left.right = TreeNode(29)
root.right.right.right.left =