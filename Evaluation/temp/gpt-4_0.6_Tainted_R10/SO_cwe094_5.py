
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

    # Get the key and object from the request arguments
    key = request.args.get('key')
    obj = request.args.get('obj')
    
    # Check if the key exists in the object
    if key in obj:
        # Return the value of the key from the object
        return str(obj[key])
    else:
        # If the key does not exist in the object, return an error message
        return 'Key not found in object'
