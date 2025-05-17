class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def compute_tree(root):
    '''
    Παίρνει ως είσοδο ένα δέντρο εκφράσεων που περιέχει (παράδειγμα του TreeNode), το διασχίζει και υπολογίζει την προκύπτουσα μαθηματική έκφραση. Αυτό το δέντρο εκφράσεων υποστηρίζει τις αριθμητικές λειτουργίες: +, -, *, /, ^, %. @param root: η ρίζα του δέντρου εκφράσεων @return: το αποτέλεσμα της μαθηματικής έκφρασης (float)
    '''
if root is None:
        return 0
    return compute_tree(root.left) + compute_tree(root.right) + root.val

