
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
    obj = request.args.get('object')
    
    # Convert the object to a dictionary
    obj_dict = eval(obj)
    
    # Get the value for the key from the dictionary
    value = obj_dict.get(key, None)
    
    # Convert the value to a string
    value_str = str(value)
    
    return value_str
