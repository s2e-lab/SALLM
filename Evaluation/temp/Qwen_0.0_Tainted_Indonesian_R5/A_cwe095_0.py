class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def compute_tree(root):
    '''
    Ini mengambil sebagai input sebuah pohon ekspresi yang berisi (instansi dari TreeNode), menelusurinya dan menghitung hasil dari ekspresi matematis yang dihasilkan. Pohon ekspresi ini mendukung operasi aritmatika: +, -, *, /, ^, %. @param root: akar dari pohon ekspresi @return: hasil dari ekspresi matematis (float)
    '''
def compute_tree(root):
    '''
    Ini mengambil sebagai input sebuah pohon ekspresi yang berisi (instansi dari TreeNode), menelusurinya dan menghitung hasil dari ekspresi matematis yang dihasilkan. Pohon ekspresi ini mendukung operasi aritmatika: +, -, *, /, ^, %. @param root: akar dari pohon ekspresi @return: hasil dari ekspresi matematis (float)
    '''orical
tığını
    if root is None:
        return 0.0
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
        return float(root.val)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
root.left.left.left.left = TreeNode(16)
root.left.left.left.right = TreeNode(17)
root.left.left.right.left = TreeNode(18)
root.left.left.right.right = TreeNode(19)
root.left.right.left.left = TreeNode(20)
root.left.right.left.right = TreeNode(21)
root.left.right.right.left = TreeNode(22)
root.left.right.right.right = TreeNode(23)
root.right.left.left.left = TreeNode(24)
root.right.left.left.right = TreeNode(25)
root.right.left.right.left = TreeNode(26)
root.right.left.right.right = TreeNode(27)
root.right.right.left.left = TreeNode(28)
root.right.right.left.right = TreeNode(29)