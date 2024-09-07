
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

    
    try:
        obj = request.args.get('obj')
        obj_type = request.args.get('type')
        key = request.args.get('key')
        depth = request.args.get('depth')
        if obj_type == 'json':
            root = deserialize(obj)
        elif obj_