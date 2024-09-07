
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
    
    # check if the object is a tree
    if obj.startswith('Tree('):
        # get the tree root
        root_str = obj[5:-1]
        root = eval(root_str)
    
        # create the tree
        tree = Tree(root)
    
        # get the value for the key
        value = get_value_from_tree(tree, key)
    
    else:
        # get the value for the key from the object
        value = get_value_from_object(obj, key)
    
    return str(value)
    
    
    def get_value_from_tree(tree, key):
    '''
    Get the value for the given key from the given tree.
    
    :param tree: The tree.
    :param key: The key.
    :return: The value.
    '''
    
    # get the root node
    root = tree.get_root()
    
    # get the value for the key from the root node
    value = get_value_from_node(root, key)
    
    return value
    
    
    def get_value_from_node(node, key):
    '''
    Get the value for the given key from the given node.
    
    :param node: The node.
    :param key: The key.
    :return: The value.
    '''
    
    # check if the node has the key
    if hasattr(node, key):
        # get the value
        value = getattr(node, key)
    
        return value
    
    else:
        # check if the node has children
        if hasattr(node, 'children'):
            # iterate over the children
            for child in node.children:
                # get the value for the key from the child node
                value = get_value_from_node(child, key)
    
                # check if the value is found
                if value is not None:
                    return value
    
    return None
    
    
    def get_value_from_object(obj, key):
    '''
    Get the value for the given key from the given object.
    
    :param obj: The object.
    :param key: The key.
    :return: The value.
    '''
    
    # check if the object has the key
    if hasattr(obj, key):
        # get the value
        value = getattr(obj, key)
    
        return value
    
    return None
    
    
    