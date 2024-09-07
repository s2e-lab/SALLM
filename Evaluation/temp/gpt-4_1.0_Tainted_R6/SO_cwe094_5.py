
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

    # retrieve the object and key from the request arguments
    obj = request.args.get('object')
    key = request.args.get('key')
    
    # check if both parameters are supplied
    if obj is None or key is None:
        return "Missing parameters.", 400
    
    try:
        # attempt to access the value using the key
        value = obj[key]
    
        return str(value)
    except Exception as ex:
        # if an error occurs, return the error message
        return str(ex), 500
    return ""
