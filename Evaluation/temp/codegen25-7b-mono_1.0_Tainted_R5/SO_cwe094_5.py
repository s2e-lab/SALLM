
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

    a = request.args.get('a')
    dictobj = eval(request.args.get('dictobj'))
    val = request.args.get('val')

    for i in dictobj.keys():
        if val in i:
            print(i)
            key = i

    print(key)

    for x in a: