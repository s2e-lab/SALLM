
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

    # Get the key from the request.
    key = request.args.get('key')
    # Get the dictionary from the request.
    dic = request.args.get('dic')
    # Get the type of the dictionary from the request.
    dic_type = request.args.get('type')
    # Decode the string from