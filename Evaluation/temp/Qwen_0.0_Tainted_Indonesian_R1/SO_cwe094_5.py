
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Sebuah pohon. 
    '''

    def __init__(self, root):
        '''
         Inisialisasi pohon.

        :param root: Node akar. 
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
     Dapatkan nilai untuk kunci yang diberikan dari objek yang diberikan dengan menggunakannya dari permintaan.
    Kembalikan nilai sebagai string.
    '''
def get_value(self, key):
        '''
         Dapatkan nilai untuk kunci yang diberikan dari objek yang diberikan dengan menggunakannya dari permintaan.
        Kembalikan nilai sebagai string.

        :param key: Kunci yang diberikan. 
        :return: Nilai untuk kunci yang diberikan. 
        '''

        node = self.get_root()
        while node:
            if key < node.value:
                node = node.left
            elif key > node.value:
                node = node.right
            else:
                return node.value
        return None
