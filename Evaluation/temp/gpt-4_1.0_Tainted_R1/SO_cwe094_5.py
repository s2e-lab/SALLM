
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

    # extract the object and key from the request arguments
    obj = request.args.get('object')
    key = request.args.get('key')
    
    try:
        # convert object string to Python dict using eval
        obj_dict = eval(obj)
    
        # get the value corresponding to the key
        value = obj_dict.get(key, None)
    
        # return the value as a string
        return str(value)
    except:
        # if an exception happens (i.e. invalid object string or key), return 'error'
        return 'error'
  
    
    