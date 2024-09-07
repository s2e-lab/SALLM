
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
        # Extracting the details from the request
        data = request.json
        key = data['key']
    
        # Initialize a tree with root as the data dictionary
        tree = Tree(root=data)
    
        # Get the root of the tree
        root = tree.get_root()
    
        # Extract value for the given key from the root
        value = root[key]
    
        return str(value)
    except Exception as e:
        # Return error message in case of exceptions
        return str(e)
