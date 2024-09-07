
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

    data = request.json
    tree = data.get("tree")
    key = data.get("key")
    
    value = None
    
    def search(node, key):
        nonlocal value
    
        if node.get("key") == key:
            value = node.get("value")
    
        for child in node.get("children", []):
            search(child, key)
    
    search(tree, key)
    
    return str(value) if value else "Key not found"
    
    