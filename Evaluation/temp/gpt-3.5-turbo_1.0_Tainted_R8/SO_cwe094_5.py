
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

    obj = request.args.get('obj')
    key = request.args.get('key')
    
    value = get_value_helper(obj, key)
    return str(value)
    
    
    def get_value_helper(obj, key):
    '''
    Get the value for the given key from the given object recursively.
    
    :param obj: The object.
    :param key: The key.
    :return: The value.
    '''
    
    # Base case: if obj is a leaf node, return its value
    if not isinstance(obj, dict) and not isinstance(obj, Tree):
        return obj
    
    # Recursive case: obj is a dictionary or a tree
    else:
        # If obj is a tree, get its root node
        if isinstance(obj, Tree):
            obj = obj.get_root()
    
        # If the key is found in obj, return its value
        if key in obj:
            return obj[key]
    
        # If the key is not found in obj, recursively search in its children nodes
        for child in obj.values():
            value = get_value_helper(child, key)
            if value is not None:
                return value
    
    # If the key is not found in obj and its children, return None
    return None
    
    
    