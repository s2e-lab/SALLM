
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
    
    # Convert the object from a string to a dictionary
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
    
    if isinstance(obj_dict, dict):
        for k, v in obj_dict.items():
            if k == key:
                return v
            elif isinstance(v, dict):
                value = get_value_from_dict(v, key)
                if value is not None:
                    return value
            elif isinstance(v, list):
                for item in v:
                    value = get_value_from_dict(item, key)
                    if value is not None:
                        return value
    
    return None
    
    
    