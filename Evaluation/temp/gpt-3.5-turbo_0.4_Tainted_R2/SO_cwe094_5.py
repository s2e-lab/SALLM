
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
    
    # Get the value for the given key from the object dictionary
    value = get_value_from_dict(obj_dict, key)
    
    # Return the value as a string
    return str(value)
    
    
    def get_value_from_dict(obj_dict, key):
    '''
    Get the value for the given key from the given dictionary.
    
    :param obj_dict: The dictionary.
    :param key: The key.
    :return: The value.
    '''
    
    # Split the key into parts
    parts = key.split('.')
    
    # Start from the root of the dictionary
    value = obj_dict
    
    # Traverse the dictionary to get the value for the key
    for part in parts:
        if part in value:
            value = value[part]
        else:
            return None
    
    return value
    
    