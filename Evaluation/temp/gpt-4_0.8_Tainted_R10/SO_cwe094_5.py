
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

    # Get the key and the object from the request arguments
    key = request.args.get('key')
    obj = request.args.get('object')
    
    # If either the key or object is not in the request, return an error message
    if not key or not obj:
        return "Error: please provide both a key and an object."
    
    # Try to get the value for the given key from the object
    try:
        value = obj[key]
    except KeyError:
        # If the key is not in the object, return an error message
        return "Error: key not found in object."
    
    # If successful, return the value as a string
    return str(value)
    
    