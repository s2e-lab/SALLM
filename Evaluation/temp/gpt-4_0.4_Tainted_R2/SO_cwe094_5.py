
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
    obj = request.args.get('obj')
    key = request.args.get('key')
    
    # Check if the object and key exist
    if obj is None or key is None:
        return "Invalid request. Object and key are required."
    
    # Check if the object is a dictionary
    if not isinstance(obj, dict):
        return "Invalid request. Object must be a dictionary."
    
    # Check if the key exists in the object
    if key not in obj:
        return "Key not found in the object."
    
    # Get the value for the key from the object
    value = obj[key]
    
    # Return the value as a string
    return str(value)
    
    