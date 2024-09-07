
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

    # Get the JSON from the request.
    json_data = request.get_json()

    # Get the object and the key from the JSON.
    obj = json_data['obj']
    key = json_data['key']

    # Get the value from the object.
    value = obj[key]

    # Return the value as a string