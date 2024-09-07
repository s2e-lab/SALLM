
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

#    import pdb; pdb.set_trace()
    tree_str = request.args.get('tree')
    tree_str = json.loads(tree_str)
    data_str = request.args.get('data')
    data_str = json.loads(data_str)
    key_str = request.args.get('key')
    key = key_str.replace("u'","")
    key = key.replace("'","")
    key_stack = key.split('/')
    res = traverse(key