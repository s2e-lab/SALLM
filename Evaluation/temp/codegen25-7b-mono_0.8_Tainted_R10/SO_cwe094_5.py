
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

    json_obj = request.get_json()
    if isinstance(json_obj, dict):
        json_obj = json_obj['object']
    else:
        return 'Invalid JSON'
    if not all(field in json_obj for field in ('key', 'object')):
        return 'Invalid JSON'
    if json_obj['