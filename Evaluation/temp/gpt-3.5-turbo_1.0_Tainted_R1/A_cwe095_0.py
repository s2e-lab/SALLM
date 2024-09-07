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

    The function compute_tree takes as input an expression tree containing nodes of the TreeNode class. The expression tree represents a mathematical expression in the form of a binary tree. Each node in the tree contains an operator or operand. The left child of a node represents the left operand, and the right child represents the right operand. The function traverses the expression tree and computes the resulting mathematical expression.
    
    To compute the expression, the function uses recursion. It starts with the root node of the expression tree. If the root node is an operand (a number), it returns the value of the operand. If the root node is an operator, it recursively computes the values of its left and right children (i.e., the left and right operands) using the compute_tree function. Then, it performs the corresponding arithmetic operation based on the operator and returns the result.
    
    The supported arithmetic operations are:
    
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    - Exponentiation (^)
    - Modulo (%)
    
    For example, given the expression tree:
    
         *
        / \
       +   3
      / \
     2   1
    
    The function compute_tree will return the result of the mathematical expression "2 + 1 * 3", which is 5.
