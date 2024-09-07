
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
    obj = request.args.get('object')
    
    # Use eval to convert the string object to an actual object
    obj = eval(obj)
    
    # Use getattr to get the value of the key from the object
    value = getattr(obj, key)
    
    # Return the value as a string
    return str(value)
