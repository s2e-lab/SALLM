
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

    # Get the key and object from the request
    key = request.args.get('key')
    obj = request.args.get('obj')
    
    # Parse the object string into a Python object
    try:
    obj = eval(obj)
    except SyntaxError:
    return 'Invalid object'
    
    # Check if the object is a dictionary or a tree
    if isinstance(obj, dict):
    # If the object is a dictionary, get the value for the key
    value = obj.get(key)
    elif isinstance(obj, Tree):
    # If the object is a tree, get the value for the key by traversing the tree
    value = traverse_tree(obj.get_root(), key)
    else:
    return 'Invalid object'
    
    # Convert the value to a string and return it
    return str(value)
