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

    if root is None:
        raise Exception('Invalid operation')
    result = None
    queue = [root]
    while queue and not result:
        root = queue.pop(0)
        val = None
        if root.left:
            queue.insert(0, root.left)
            if root.left.val not in ['/','*','^','%']:
                val = root.left.val
        elif root.right:
            queue.insert(0, root.right)
            if root.right.