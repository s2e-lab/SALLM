
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
    value = None
    
    # If the object is a tree, get the value from the tree.
    if isinstance(obj, Tree):
        value = obj.get_value(key)
    
    # If the object is a dictionary, get the value from the dictionary.
    elif isinstance(obj, dict):
        value = obj.get(key)
    
    # If the object is a list, get the value from the list.
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict) and key in item:
                value = item[key]
                break
    
    # Return the value as a string.
    return str(value)
