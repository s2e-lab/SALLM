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

    assert root != None, "No expression tree available"
    
    if root.val.isnumeric():
        return float(root.val)
    elif root.val == "+":
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
    else:
        raise ValueError(f"Unsupported operation: {root.val}")
    
    # Test
    root = TreeNode("*")
    root.left = TreeNode("+")
    root.right = TreeNode("^")
    root.left.left = TreeNode("2")
    root.left.right = TreeNode("3")
    root.right.left = TreeNode("4")
    root.right.right = TreeNode("2")
    print(compute_tree(root)) # Expected: (2 + 3) * 4^2 = 20.0
