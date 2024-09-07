
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
    
    # convert the object string to a dictionary
    obj = eval(obj)
    
    # get the value for the given key from the object
    value = get_value_from_object(obj, key)
    
    return str(value)
    
    
    def get_value_from_object(obj, key):
    '''
    Get the value for the given key from the given object.
    If the key is not found, return None.
    
    :param obj: The object.
    :param key: The key.
    :return: The value.
    '''
    
    # if the object is a dictionary, use the get() method to get the value
    if type(obj) == dict:
        return obj.get(key)
    
    # if the object is a list or tuple, use indexing to get the value
    if type(obj) == list or type(obj) == tuple:
        try:
            index = int(key)
            return obj[index]
        except ValueError:
            return None
    
    # if the object is a tree, use the get_value() method of the root node
    if type(obj) == Tree:
        return obj.get_root().get_value(key)
    
    return None
