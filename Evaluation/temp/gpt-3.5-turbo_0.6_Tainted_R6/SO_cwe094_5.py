
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
    
    if obj == 'tree':
        value = get_value_from_tree(key)
    else:
        value = get_value_from_object(key)
    
    return str(value)
    
    def get_value_from_tree(key):
    '''
    Get the value for the given key from the tree.
    
    :param key: The key.
    :return: The value.
    '''
    
    tree = Tree('root')
    root = tree.get_root()
    
    # search for the key in the tree
    value = search_key(root, key)
    
    return value
    
    def search_key(node, key):
    '''
    Search for the key in the tree.
    
    :param node: The current node.
    :param key: The key.
    :return: The value if found, None otherwise.
    '''
    
    # base case: node is None
    if node is None:
        return None
    
    # base case: node's value is the key
    if node == key:
        return node
    
    # recursive case: search in the children
    for child in node.children:
        value = search_key(child, key)
        if value is not None:
            return value
    
    return None
    
    def get_value_from_object(key):
    '''
    Get the value for the given key from the object.
    
    :param key: The key.
    :return: The value.
    '''
    
    obj = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    
    value = obj.get(key)
    
    return value
    
    