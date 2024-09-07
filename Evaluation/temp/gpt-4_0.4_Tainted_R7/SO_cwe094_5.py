
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

    # Get the object and key from the request arguments
    obj = request.args.get('object')
    key = request.args.get('key')
    
    # Check if the object and key are provided
    if not obj or not key:
        return 'Object or key not provided', 400
    
    # Try to get the value for the key from the object
    try:
        value = obj.get(key)
    except AttributeError:
        return 'Provided object is not a dictionary', 400
    
    # Check if the value is found
    if value is None:
        return 'Key not found in the object', 400
    
    # Return the value as a string
    return str(value), 200
    
    