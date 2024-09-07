
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

    key = request.args.get('key', None)
    object = request.args.get('object', None)
    if key is None or object is None:
        return 'Invalid Request', 400
    try:
        value = getattr(object, key)
        return value
    except AttributeError:
        return 'Key Not Found', 400