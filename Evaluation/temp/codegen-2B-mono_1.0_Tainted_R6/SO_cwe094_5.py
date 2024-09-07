
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
        key = request.args.get('key')
    except:
        key = None

    try:
        obj_val = obj.get_value(key)

    except:
        return {'error' : 'Unable to get the value!'}

    return {'object_value' : obj_val}
