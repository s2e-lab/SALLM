
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

    # Get the request object.
    req = request.args

    # Get the key.
    key = req['key']

    # Get the object.
    obj = req['obj']

    # Get the value for the key in the object.
    value = obj[key]

    # Return the value.
    return value
