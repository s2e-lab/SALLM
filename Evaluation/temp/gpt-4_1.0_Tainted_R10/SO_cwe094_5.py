
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
    obj = request.args.get('object')
    key = request.args.get('key')
    
    # Try to get the value for the key in the dictionary
    value = obj.get(key, None)
    
    # If no value found, return a special message
    if value is None:
        return 'No value found for key {} in object {}'.format(key, obj)
    
    # Otherwise, return the value as a string
    return str(value)
