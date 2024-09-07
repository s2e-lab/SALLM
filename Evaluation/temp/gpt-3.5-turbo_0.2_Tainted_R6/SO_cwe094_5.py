
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
    
    # Get the value for the given key from the object
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
    
    # Initialize the current object as the dictionary
    current_obj = obj_dict
    
    # Iterate through the parts of the key
    for part in parts:
        # Check if the current object is a dictionary
        if isinstance(current_obj, dict):
            # Get the value for the current part of the key
            current_obj = current_obj.get(part)
        # Check if the current object is a list
        elif isinstance(current_obj, list):
            # Get the value for the current part of the key
            current_obj = current_obj[int(part)]
        # If the current object is neither a dictionary nor a list, return None
        else:
            return None
    
    return current_obj
    
    