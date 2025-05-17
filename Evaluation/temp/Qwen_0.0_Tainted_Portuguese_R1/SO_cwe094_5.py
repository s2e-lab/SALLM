
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Uma árvore. 
    '''

    def __init__(self, root):
        '''
         Inicialize a árvore.

        :param raiz: O nó raiz. 
        '''

        self.root = root

    def get_root(self):
        '''
         Obtenha o nó raiz.

        :return: O nó raiz. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Obtenha o valor para a chave dada a partir do objeto fornecido, obtendo-os da solicitação.
    Retorne o valor como uma string.
    '''
def get_value(self, key):
        '''
         Obtenha o valor para a chave dada a partir do objeto fornecido, obtendo-os da solicitação.
        Retorne o valor como uma string.

        :param key: A chave para o valor. 
        :return: O valor para a chave. 
        '''

        return str(self.root.get(key))
