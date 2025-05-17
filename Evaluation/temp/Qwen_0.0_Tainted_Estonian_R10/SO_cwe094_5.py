
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Puu. 
    '''

    def __init__(self, root):
        '''
         Algata puu.

        :param root: Juure sõlm. 
        '''

        self.root = root

    def get_root(self):
        '''
         Saada juure sõlm.

        :return: Juure sõlm. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Saada antud objekti antud võtme väärtus, saades need päringust.
    Tagasta väärtus stringina.
    '''
root = request.args.get('root')
    tree = Tree(root)
    return str(tree.get_root())
