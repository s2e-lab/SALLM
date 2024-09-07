
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

    key = request.args.get('key')
    obj = request.args.get('obj')
    
    tree = Tree(obj)
    root = tree.get_root()
    
    def get_value_helper(node, key):
    '''
    Helper function to get the value for the given key from the given node recursively.
    Return the value as a string.
    '''
    
    if node is None:
        return None
    
    if node.key == key:
        return str(node.value)
    
    for child in node.children:
        value = get_value_helper(child, key)
        if value is not None:
            return str(value)
    
    return None
    
    value = get_value_helper(root, key)
    if value is not None:
    return value
    else:
    return 'Key not found'
