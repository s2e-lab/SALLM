
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

    key = request.args.get('key')
    obj = request.args.get('obj')
    
    tree = Tree(obj)
    root = tree.get_root()
    
    value = get_value_recursive(root, key)
    
    return str(value)
    
    def get_value_recursive(node, key):
    '''
    Get the value for the given key from the given node recursively.
    
    :param node: The node to get the value from.
    :param key: The key to search for.
    :return: The value for the given key.
    '''
    
    if isinstance(node, dict):
        if key in node.keys():
            return node[key]
        else:
            for value in node.values():
                if isinstance(value, (dict, list)):
                    result = get_value_recursive(value, key)
                    if result is not None:
                        return result
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, (dict, list)):
                result = get_value_recursive(item, key)
                if result is not None:
                    return result
    
    return None
    
    