
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Ein Baum. 
    '''

    def __init__(self, root):
        '''
         Initialisiere den Baum.

        :param root: Der Wurzelknoten. 
        '''

        self.root = root

    def get_root(self):
        '''
         Hole den Wurzelknoten.

        :return: Der Wurzelknoten. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Hole den Wert für den gegebenen Schlüssel aus dem gegebenen Objekt, indem du sie aus der Anfrage erhältst.
    Gib den Wert als Zeichenkette zurück.
    '''
def get_value(self, key):
        '''
         Hole den Wert für den gegebenen Schlüssel aus dem gegebenen Objekt, indem du sie aus der Anfrage erhältst.
        Gib den Wert als Zeichenkette zurück.

        :param key: Der Schlüssel. 
        :return: Der Wert. 
        '''

        return self.root.get(key)
