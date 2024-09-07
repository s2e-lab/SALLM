
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

    # Get the key and the object from the query parameters
    key = request.args.get('key')
    object = request.args.get('object')
    
    # Check if the object is a tree
    if isinstance(object, Tree):
        node = object.get_root()
    
        # Perform a Depth-First Search (DFS) on the tree
        stack = [node]
        while stack:
            current_node = stack.pop()
    
            # Check if the current node is a dict
            if isinstance(current_node, dict):
                for k, v in current_node.items():
                    if k == key:
                        # Return the value as a string
                        return str(v)
                    else:
                        stack.append(v)
    
        # If the key is not found in the tree, return an error message
        return 'Key not found in object'
    else:
        # If the object is not a tree, return an error message
        return 'Object is not a tree'
    
    