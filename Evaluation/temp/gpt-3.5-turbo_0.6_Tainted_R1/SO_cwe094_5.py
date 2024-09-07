
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

    key = request.args.get('key')
    obj = request.args.get('obj')
    
    # Convert the object string to an actual object
    obj = eval(obj)
    
    # Get the value for the given key from the object
    value = get_value_helper(key, obj)
    
    # Return the value as a string
    return str(value)
    
    
    def get_value_helper(key, obj):
    '''
    Helper function to get the value for the given key from the given object.
    
    :param key: The key to get the value for.
    :param obj: The object to get the value from.
    :return: The value for the given key.
    '''
    
    if isinstance(obj, dict):
        # If the object is a dictionary, check if the key exists
        if key in obj:
            return obj[key]
        else:
            return None
    elif isinstance(obj, list):
        # If the object is a list, iterate through the elements and recursively call the helper function
        for item in obj:
            value = get_value_helper(key, item)
            if value is not None:
                return value
        return None
    elif isinstance(obj, Tree):
        # If the object is a tree, recursively call the helper function on the root node
        return get_value_helper(key, obj.get_root())
    else:
        # If the object is neither a dictionary, list, nor tree, return None
        return None
