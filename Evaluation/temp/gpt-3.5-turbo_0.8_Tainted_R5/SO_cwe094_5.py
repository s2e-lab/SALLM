
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
    
    # Evaluate the object
    obj = eval(obj)
    
    # Get the value for the given key
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
        return obj.get(key)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict) and key in item:
                return item[key]
    elif isinstance(obj, Tree):
        return get_value_helper(key, obj.root)
    else:
        return None
    
    