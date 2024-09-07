
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


#   Get the query string of the request
    q_str = request.query_string
#   Split it on '='
    q_list = q_str.split('=')

#   get the value of the tree
    cld = tree.get_root()
#   Set to root node
    cl_nr = cld

