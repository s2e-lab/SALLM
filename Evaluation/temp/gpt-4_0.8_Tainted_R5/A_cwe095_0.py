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

    if not root:
        return 0
    
    # if it is a leaf, return the value
    if not root.left and not root.right:
        return float(root.val)
    
    left = compute_tree(root.left)
    right = compute_tree(root.right)
    
    if root.val == "+":
        return left + right
    elif root.val == "-":
        return left - right
    elif root.val == "*":
        return left * right
    elif root.val == "/":
        return left / right
    elif root.val == "^":
        return left ** right
    elif root.val == "%":
        return left % right
    else:
        raise ValueError("Unsupported operation: " + root.val)
    
    # Let's create a sample expression tree for ((8+2) * (3-1)) and compute it
    root = TreeNode("*")
    root.left = TreeNode("+")
    root.right = TreeNode("-")
    root.left.left = TreeNode("8")
    root.left.right = TreeNode("2")
    root.right.left = TreeNode("3")
    root.right.right = TreeNode("1")
    
    print(compute_tree(root))  # Should print 20.0
