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

    if root.val.isnumeric():
        return int(root.val)
    
    if root.val == "+":
        return compute_tree(root.left) + compute_tree(root.right)
    elif root.val == "-":
        return compute_tree(root.left) - compute_tree(root.right)
    elif root.val == "*":
        return compute_tree(root.left) * compute_tree(root.right)
    elif root.val == "/":
        return compute_tree(root.left) / compute_tree(root.right)
    elif root.val == "^":
        return compute_tree(root.left) ** compute_tree(root.right)
    elif root.val == "%":
        return compute_tree(root.left) % compute_tree(root.right)
    
    # Example usage:
    
    # Construct the following expression tree:
    #     *
    #    / \
    #   +   -
    #  / \ / \
    # 3  2 4  5
    
    root = TreeNode("*")
    root.left = TreeNode("+")
    root.right = TreeNode("-")
    root.left.left = TreeNode("3")
    root.left.right = TreeNode("2")
    root.right.left = TreeNode("4")
    root.right.right = TreeNode("5")
    
    print(compute_tree(root))  # Outputs: 20
