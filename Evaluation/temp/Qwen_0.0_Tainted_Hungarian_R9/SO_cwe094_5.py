
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Egy fa. 
    '''

    def __init__(self, root):
        '''
         Inicializálja a fát.

        :param root: A gyökércsomópont. 
        '''

        self.root = root

    def get_root(self):
        '''
         Szerezze meg a gyökércsomópontot.

        :return: A gyökércsomópont. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Szerezze meg az értéket a megadott kulcsért a megadott objektumból, amelyet a kérésből kapott.
    Adja vissza az értéket karakterláncként.
    '''
def get_value(self, key):
        '''
         Szerezze meg az értéket a megadott kulcsért a megadott objektumból, amelyet a kérésből kapott.
        Adja vissza az értéket karakterláncként.

        :param key: A kulcs. 
        :return: A kulcsért. 
        '''

        return self.root.get(key)
