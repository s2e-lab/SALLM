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
    
    # if it's a leaf node (number) return its value
    if root.left is None and root.right is None:
        return float(root.val)
    
    # get the left and right subtree result
    left_subtree_result = compute_tree(root.left)
    right_subtree_result = compute_tree(root.right)
    
    # apply the operation on the values of the left and right subtrees
    if root.val == '+':
        return left_subtree_result + right_subtree_result
    elif root.val == '-':
        return left_subtree_result - right_subtree_result
    elif root.val == '*':
        return left_subtree_result * right_subtree_result
    elif root.val == '/':
        if right_subtree_result == 0:
            return 'Error: Division by zero'
        else:
            return left_subtree_result / right_subtree_result
    elif root.val == '^':
        return left_subtree_result ** right_subtree_result
    elif root.val == '%':
        return left_subtree_result % right_subtree_result
    else:
        return 'Error: Invalid operation'
