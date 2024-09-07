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

    result = float(root.val)
    if root.left:
        node_left = compute_tree(root.left)
        if hasattr(node_left, 'val'):
            if root.val.lstrip('-').isdigit():
                node_left = -node_left
            if node_left == 0:
                return float(root.left.val)
            else:
                result = node_left + node_left * result
        else:
            print("no left node in current node")
