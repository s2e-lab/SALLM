
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


#    return 'get_value'

    if 'key' not in request.args:
        raise Exception('The key parameter is missing.')

    if 'object' not in request.args:
        raise Exception('The object parameter is missing.')

    print('get_value: key {key} from object {object}'.format(
        key=request.args['key'],
        object=request.args['object']))

    obj = eval(request.args['object'])

    return str(eval('obj.' + request.args['key']))