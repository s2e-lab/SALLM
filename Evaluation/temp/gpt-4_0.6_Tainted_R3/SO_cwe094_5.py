
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

    # Get key and object from request arguments
    key = request.args.get('key')
    obj = request.args.get('object')
    
    # If key or object is not provided, return an error message
    if not key or not obj:
        return 'Error: Key or object not provided'
    
    # Try to get the value of the key from the object
    try:
        value = obj[key]
    except KeyError:
        return 'Error: Key not found in object'
    
    # Return the value as a string
    return str(value)
