
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

    # Get the object from the request
    obj = request.args.get('object')
    # Get the key from the request
    key = request.args.get('key')
    
    # Check if the object and key are not None
    if obj is not None and key is not None:
        # Try to get the value for the key from the object
        try:
            value = obj[key]
        # If the key does not exist in the object
        except KeyError:
            return "Key does not exist in the object"
        # Return the value as a string
        return str(value)
    # If the object or key is None
    else:
        return "Object or key is missing"
    
    