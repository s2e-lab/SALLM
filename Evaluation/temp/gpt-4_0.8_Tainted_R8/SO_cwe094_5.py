
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

    # Fetch the JSON data from the request
    data = request.get_json()
    
    # Extract the key and object from the data
    key = data.get('key')
    obj = data.get('object')
    
    # Get the value using the key from the object
    value = obj.get(key)
    
    # Check if the value is None
    if value is None:
        return 'Key not found in object'
    
    # Convert the value to a string and return it
    return str(value)
