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
        return 0
    
    if root.val.isdigit(): 
        return float(root.val)
    
    else: 
        left = compute_tree(root.left) 
        right = compute_tree(root.right) 
    
        if root.val == '+':
            return left + right
    
        elif root.val == '-':
            return left - right
    
        elif root.val == '*':
            return left * right 
    
        elif root.val == '/':
            if right == 0: 
                raise ValueError('Division by zero is not supported')
            return left / right 
    
        elif root.val == '^':
            return left ** right  
    
        elif root.val == '%':
            return left % right  
        
        else:
            raise ValueError('Operator not supported')
    
    # Example usage:
    # 4 + (9 - 7) * 2
    # structured as a Binary Expression Tree: 
    
    #      "+"
    #     /   \
    #  "4"     "*"
    #        /     \
    #     "-"      "2"
    #    /   \
    # "9"   "7"
    
    # root = TreeNode("+")
    # root.left = TreeNode("4")
    # root.right = TreeNode("*")
    # root.right.left = TreeNode("-")
    # root.right.left.left = TreeNode("9")
    # root.right.left.right = TreeNode("7")
    # root.right.right = TreeNode("2")
    
    # print(compute_tree(root))  # prints: 8.0
    
