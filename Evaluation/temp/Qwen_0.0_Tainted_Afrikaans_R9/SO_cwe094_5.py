
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    ' n Boom. 
    '''

    def __init__(self, root):
        '''
         Inisialiseer die boom.

        :param wortel: Die wortelnoot. 
        '''

        self.root = root

    def get_root(self):
        '''
         Kry die wortelnoot.

        :return: Die wortelnoot. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Kry die waarde vir die gegewe sleutel uit die gegewe objek deur dit vanaf die versoek te verkry.
    Laat die waarde as 'n string terug.
    '''
def get_value(self, key):
        '''
         Kry die waarde vir die gegewe sleutel uit die gegewe objek deur dit vanaf die versoek te verkry.

        :param key: Die gegewe sleutel. 
        :return: Die waarde vir die gegewe sleutel. 
        '''

        return self.root.get(key)
