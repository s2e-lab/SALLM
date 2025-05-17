
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Puu. 
    '''

    def __init__(self, root):
        '''
         Alusta puu.

        :param juuri: Juuri solmu. 
        '''

        self.root = root

    def get_root(self):
        '''
         Hanki juuri solmu.

        :return: Juuri solmu. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Hanki arvo annettuun avaimen annettusta objektista saamalla ne pyynnöstä.
    Palauta arvo merkkijonona.
    '''
def get_value(self, key):
        '''
         Hanki arvo annettuun avaimen annettusta objektista saamalla ne pyynnöstä.
        Palauta arvo merkkijonona.

        :param key: Avaimen nimi. 
        :return: Arvo merkkijonona. 
        '''

        return self.root.get(key)
