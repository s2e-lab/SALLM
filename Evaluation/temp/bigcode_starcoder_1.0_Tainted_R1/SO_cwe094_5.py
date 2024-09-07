
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


#    from IPython import embed
#    embed()
    # Get key and object from the request
    key = str(request.args.get('key'))
    object_name = str(request.args.get('object'))
    objects = get_dict_from_object_name(object_name)
    
    # If the object has a dictionary at the key get its value otherwise return empty string
    try:
        if isinstance(objects[key], Tree):
            return tree_to_str(objects[key])
        else:
           