
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Satu kayu. 
    '''

    def __init__(self, root):
        '''
         Inisialisasi kayu.

        :param akar: Node akar. 
        '''

        self.root = root

    def get_root(self):
        '''
         Dapatkan node akar.

        :return: Node akar. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Dapatkan nilai untuk kunci yang diberikan dari objek yang diberikan dengan mengikutinya dari permintaan.
    Kembalikan nilai sebagai string.
    '''
def get_value(self, key):
        '''
         Dapatkan nilai untuk kunci yang diberikan dari objek yang diberikan dengan mengikutinya dari permintaan.

        :param key: Kunci yang diberikan. 
        :return: Nilai untuk kunci yang diberikan. 
        '''

        return self.root.get_value(key)
