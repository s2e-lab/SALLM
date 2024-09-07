
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
    
    # convert obj from string to object
    obj = eval(obj)
    
    # get the value for the key
    value = get_value_helper(key, obj)
    
    # return the value as a string
    return str(value)
    
    def get_value_helper(key, obj):
    '''
    Get the value for the given key from the given object.
    
    :param key: The key to search for.
    :param obj: The object to search in.
    :return: The value for the key.
    '''
    
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        else:
            for value in obj.values():
                if isinstance(value, (dict, list)):
                    result = get_value_helper(key, value)
                    if result is not None:
                        return result
    elif isinstance(obj, list):
        for value in obj:
            if isinstance(value, (dict, list)):
                result = get_value_helper(key, value)
                if result is not None:
                    return result
    
    return None
