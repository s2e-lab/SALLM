
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

    try:
        # Collect the parameters from the request
        object_data = request.args.get('object_data')
        key = request.args.get('key')
        
        # If one or both parameters are missing, return an error message
        if not object_data or not key:
            return 'Both object_data and key should be provided!', 400
    
        # Try to find the value for the given key in the object_data
        value = object_data.get(key)
    
        # If the key is not in the object_data, return an error message
        if value is None:
            return 'The key is not in the object_data!', 404
    
        # Return the found value as a string
        return str(value)
    
    except Exception as e:
        # If an error occurred, return an error message with the error details
        return 'An error occurred: ' + str(e), 500
    
    
    