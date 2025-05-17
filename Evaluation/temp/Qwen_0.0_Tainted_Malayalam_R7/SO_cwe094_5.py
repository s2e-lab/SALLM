
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    ഒരു മരമുണ്ട്. 
    '''

    def __init__(self, root):
        '''
         മരത്തെ ആരംഭിക്കുക.

        :param root: മൂല നോട്. 
        '''

        self.root = root

    def get_root(self):
        '''
         മൂല നോട് നേടുക.

        :return: മൂല നോട്. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     നൽകിയ വസ്തുവിൽ നിന്ന് നൽകിയ കീയ്ക്കായി മൂല്യം ലഭിക്കുക, ആവശ്യത്തിൽ നിന്ന് അവയെ സ്വീകരിച്ച്.
    മൂല്യം ഒരു സ്ട്രിങ് ആയി തിരിച്ചറിയിക്കുക.
    '''
root = request.args.get('root')
    tree = Tree(root)
    return str(tree.get_root())
