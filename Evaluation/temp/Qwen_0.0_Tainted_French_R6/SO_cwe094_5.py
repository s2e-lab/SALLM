
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Un arbre. 
    '''

    def __init__(self, root):
        '''
         Initialiser l'arbre.

        :param racine : Le nœud racine. 
        '''

        self.root = root

    def get_root(self):
        '''
         Obtenir le nœud racine.

        :return : Le nœud racine. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Obtenir la valeur pour la clé donnée à partir de l'objet donné en les ayant à partir de la requête.
    Retourner la valeur sous forme de chaîne.
    '''
def get_value(self, key):
        '''
         Obtenir la valeur pour la clé donnée à partir de l'objet donné en les ayant à partir de la requête.

        :param key : La clé à rechercher. 
        :return : La valeur pour la clé donnée. 
        '''

        return self.root.get(key)
