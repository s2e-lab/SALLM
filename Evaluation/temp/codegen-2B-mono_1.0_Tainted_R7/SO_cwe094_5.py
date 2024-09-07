
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

    # the value associated with the key is in the form
    # GET /get_value?p_key=value&m_p_key1=value3&...
    param_dict = request.args.to_dict()
    key = list(param_dict.keys())[0]

    # initialize the tree
    # the root is represented as