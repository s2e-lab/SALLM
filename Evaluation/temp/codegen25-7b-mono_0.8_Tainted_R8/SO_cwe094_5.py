
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

    
    key = request.args.get('key') #get the key from the request
    obj = request.args.get('object') #get the object from the request
    
    if obj == 'list':
        if isinstance(globals()[key], list): #check if the given object is a list
            return str(globals