
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

    # get the data from the request
    data = request.json
    
    # get the object and the key from the data
    object = data.get('object')
    key = data.get('key')
    
    # get the value for the given key from the given object
    value = object.get(key)
    
    # return the value as a string
    return str(value)
