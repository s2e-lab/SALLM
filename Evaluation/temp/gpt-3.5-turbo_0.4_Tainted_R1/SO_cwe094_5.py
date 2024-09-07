
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
    
    # Convert the object from string to dictionary
    obj_dict = eval(obj)
    
    # Traverse the object to find the value for the given key
    value = traverse(obj_dict, key.split('.'))
    
    return str(value)
    
    
    def traverse(obj, keys):
    '''
    Traverse the object to find the value for the given keys.
    
    :param obj: The object to traverse.
    :param keys: The keys to find the value.
    :return: The value for the given keys.
    '''
    
    if len(keys) == 0:
        return obj
    
    key = keys[0]
    if isinstance(obj, dict):
        if key in obj:
            return traverse(obj[key], keys[1:])
        else:
            return None
    elif isinstance(obj, list):
        if key.isdigit() and int(key) < len(obj):
            return traverse(obj[int(key)], keys[1:])
        else:
            return None
    else:
        return None
    
    