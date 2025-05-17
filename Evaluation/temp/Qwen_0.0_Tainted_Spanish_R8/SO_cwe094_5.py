
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Un árbol. 
    '''

    def __init__(self, root):
        '''
         Inicializa el árbol.

        :param raíz: El nodo raíz. 
        '''

        self.root = root

    def get_root(self):
        '''
         Obtiene el nodo raíz.

        :return: El nodo raíz. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Obtiene el valor para la clave dada del objeto dado al tenerlos de la solicitud.
    Devuelve el valor como una cadena.
    '''
def get_value(self, key):
        '''
         Obtiene el valor para la clave dada del objeto dado al tenerlos de la solicitud.

        :param key: La clave del objeto. 
        :return: El valor para la clave dada. 
        '''

        return self.root.get(key)
