
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

    name = request.args.get('name', None)
    tree = get_tree()
    print(name)
    print(tree)
    if name is None:
        raise Exception("Error: The key must be given.")
    root = tree.get_root()
    found = search(name, root)
    print(found)
    