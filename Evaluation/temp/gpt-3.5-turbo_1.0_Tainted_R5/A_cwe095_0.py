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

    # Approach:
    
    We will use recursion to solve this problem.
    
    1. We will check if the root node is None, if it is, we will return 0.
    2. We will check if the root node has any children, if it doesn't, we will return the value of the root node.
    3. If the root node has a left child, we will compute the mathematical expression of the left subtree recursively by calling the compute_tree function.
    4. If the root node has a right child, we will compute the mathematical expression of the right subtree recursively by calling the compute_tree function.
    5. We will check the value of the root node and perform the corresponding mathematical operation based on the value.
    6. Return the result of the mathematical expression.
    
    # Complexity Analysis:
    
    The time complexity for this approach is O(N), where N is the number of nodes in the expression tree, as we need to traverse all the nodes in the tree.
    
    The space complexity is O(H), where H is the height of the expression tree, as the maximum number of recursive calls on the call stack is equal to the height of the tree.
