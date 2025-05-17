
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Bir ağaç. 
    '''

    def __init__(self, root):
        '''
         Ağacı başlatın.

        :param root: Kök düğüm. 
        '''

        self.root = root

    def get_root(self):
        '''
         Kök düğümü alın.

        :return: Kök düğüm. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Verilen nesneden verilen anahtar için değeri, istekte bulunarak alın.
    Değeri bir dize olarak döndürün.
    '''
def get_value(self, key):
        '''
         Verilen nesneden verilen anahtar için değeri, istekte bulunarak alın.

        :param key: Anahtar. 
        :return: Değer. 
        '''

        return self.root.get(key)
