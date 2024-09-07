
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

    
    # TODO
    # Use request.args.get('') to get the key and value.
    # You need to handle a few edge cases:
    # 1. There is no key.
    # 2. The key is not in the object.
    # 3. The key is in the object, but it is None.
    # 4