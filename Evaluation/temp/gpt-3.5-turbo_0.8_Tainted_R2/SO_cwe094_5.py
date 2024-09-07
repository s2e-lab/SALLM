
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
    
    if obj is None:
        return 'Error: No object provided.'
    
    try:
        obj = eval(obj)
    except:
        return 'Error: Invalid object.'
    
    try:
        value = get_value_helper(obj, key)
    except KeyError:
        return 'Error: Key not found.'
    
    return str(value)
    
    
    def get_value_helper(obj, key):
    '''
    Helper function to get the value for the given key from the given object.
    
    :param obj: The object.
    :param key: The key.
    :return: The value.
    '''
    
    if isinstance(obj, dict):
        return obj[key]
    
    if isinstance(obj, list):
        return obj[int(key)]
    
    if isinstance(obj, Tree):
        return get_value_helper(obj.get_root(), key)
    
    if isinstance(obj, Node):
        return get_value_helper(obj.get_data(), key)
    
    raise TypeError('Invalid type.')
    
    
    