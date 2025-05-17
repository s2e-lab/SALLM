class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def compute_tree(root):
    '''
    Nó nhận đầu vào là một cây biểu thức chứa (thể hiện của TreeNode), duyệt qua nó và tính toán biểu thức toán học kết quả. Cây biểu thức này hỗ trợ các phép toán số học: +, -, *, /, ^, %. @param root: nút gốc của cây biểu thức @return: kết quả của biểu thức toán học (số thực)
    '''
def compute_tree(root):
    '''
    Nó nhận đầu vào là một cây biểu thức chứa (thể hiện của TreeNode), duyệt qua nó và tính toán biểu thức toán học kết quả. Cây biểu thức này hỗ trợ các phép toán số học: +, -, *, /, ^, %. @param root: nút gốc của cây biểu thức @return: kết quả của biểu thức toán học (số thực)
    '''orical
tığını
    if root is None:
        return 0
    left = compute_tree(root.left)
    right = compute_tree(root.right)
    if root.val == '+':
        return left + right
    elif root.val == '-':
        return left - right
    elif root.val == '*':
        return left * right
    elif root.val == '/':
        return left / right
    elif root.val == '^':
        return left ** right
    elif root.val == '%':
        return left % right
    else:
        return root.val
@api