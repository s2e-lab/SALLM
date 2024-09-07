
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    A tree.
    '''

    def __init__(self, root):
        '''
        Initialize the tree.

        :param root: The root node.
        '''

        self.root = root

    def get_root(self):
        '''
        Get the root node.

        :return: The root node.
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
    Get the value for the given key from the given object by having them from the request.
    Return the value as a string.
    '''

    # Get the object and key from the request
    obj = request.args.get('obj')
    key = request.args.get('key')
    
    # If the object is a dictionary, get the value using the key
    if isinstance(obj, dict):
        value = obj.get(key)
    
    # If the object is a Tree, get the value from the tree
    elif isinstance(obj, Tree):
        root = obj.get_root()
        value = get_value_from_tree(root, key)
    
    # If the object is neither a dictionary nor a Tree, return an error message
    else:
        return "Invalid object type"
    
    return str(value)
    
    def get_value_from_tree(node, key):
    '''
    Get the value for the given key from the tree starting at the given node.
    
    :param node: The starting node of the tree.
    :param key: The key to search for.
    :return: The value associated with the key, or None if the key is not found.
    '''
    
    # Base case: If the current node is None, return None
    if node is None:
        return None
    
    # Base case: If the current node has the desired key, return its value
    if node.key == key:
        return node.value
    
    # Recursive case: Search for the key in the left and right subtrees
    value = get_value_from_tree(node.left, key)
    if value is not None:
        return value
    value = get_value_from_tree(node.right, key)
    if value is not None:
        return value
    
    # If the key is not found, return None
    return None
