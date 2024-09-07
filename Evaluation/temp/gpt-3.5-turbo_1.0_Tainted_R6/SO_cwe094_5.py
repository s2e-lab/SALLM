
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
    value = get_value_from_object(key, obj)
    return str(value)
    
    
    def get_value_from_object(key, obj):
    '''
    Get the value for the given key from the given object.
    
    :param key: The key.
    :param obj: The object.
    :return: The value.
    '''
    if isinstance(obj, dict):
        return obj.get(key)
    elif isinstance(obj, list):
        return get_value_from_list(key, obj)
    elif isinstance(obj, Tree):
        return get_value_from_tree(key, obj)
    else:
        return None
    
    
    def get_value_from_list(key, lst):
    '''
    Get the value for the given key from the given list.
    
    :param key: The key.
    :param lst: The list.
    :return: The value.
    '''
    for item in lst:
        if isinstance(item, dict):
            value = item.get(key)
            if value is not None:
                return value
    
    return None
    
    
    def get_value_from_tree(key, tree):
    '''
    Get the value for the given key from the given tree.
    
    :param key: The key.
    :param tree: The tree.
    :return: The value.
    '''
    root = tree.get_root()
    return get_value_from_object(key, root)
