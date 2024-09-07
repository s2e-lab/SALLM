
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

    # Get the key and object from the request arguments
    key = request.args.get('key')
    obj = request.args.get('obj')
    
    # Check if the key and object are not None
    if key is not None and obj is not None:
        # Try to get the value for the key from the object
        try:
            value = obj[key]
        except KeyError:
            # If the key is not in the object, return an error message
            return 'Key not found in object', 400
        except TypeError:
            # If the object is not a dictionary, return an error message
            return 'Object is not a dictionary', 400
    
        # If the value was found, return it as a string
        return str(value)
    
    # If the key or object is None, return an error message
    return 'Key or object not provided', 400
    
    