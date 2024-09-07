
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

    # The key to check for in the json.
    key = request.args.get('key')

    # The object to check in.
    obj = request.args.get('obj')

    # Turn the object into a dictionary.
    treeDict = json.loads(obj)

    # Return the value.
    return treeDict.get