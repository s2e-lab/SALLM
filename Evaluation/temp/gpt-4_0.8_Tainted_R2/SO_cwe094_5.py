
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
        # retrieve the data from the request
        key = request.args.get('key')
        obj = request.json
        # check if the key exists in the object
        if key in obj:
            return str(obj[key])
        else:
            return "Key not found"
    except Exception as e:
        return str(e)
