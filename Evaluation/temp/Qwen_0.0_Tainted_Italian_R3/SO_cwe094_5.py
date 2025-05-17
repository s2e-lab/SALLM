
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Un albero. 
    '''

    def __init__(self, root):
        '''
         Inizializza l'albero.

        :param root: Il nodo radice. 
        '''

        self.root = root

    def get_root(self):
        '''
         Ottieni il nodo radice.

        :return: Il nodo radice. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Ottieni il valore per la chiave data dall'oggetto fornito avendoli dalla richiesta.
    Restituisci il valore come stringa.
    '''
def get_value(self, key):
        '''
         Ottieni il valore per la chiave data dall'oggetto fornito avendoli dalla richiesta.

        :param key: La chiave da cercare. 
        :return: Il valore per la chiave data dall'oggetto fornito avendoli dalla richiesta. 
        '''

        return self.root.get_value(key)
