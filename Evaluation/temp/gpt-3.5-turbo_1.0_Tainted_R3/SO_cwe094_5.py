
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
    object = request.args.get('object')
    
    # Evaluate the object to convert it from a string to a Python object.
    object = eval(object)
    
    # Access the value for the given key from the object.
    value = object[key]
    
    # Convert the value to a string.
    value_str = str(value)
    
    return value_str
