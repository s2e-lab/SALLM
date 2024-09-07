
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


#     if not request.args or not request.args['object'] or not request.args['key']:
#         return 'Error: Please send both an object and a key.'

    object = request.args.get('object')
    key = request.args.get('key')

    # Split the object string to a list of its components
    object_list = object.split('.')
    parent_object = object_list[0]
    child_object = object_list[1]
    grandchild_object = object_