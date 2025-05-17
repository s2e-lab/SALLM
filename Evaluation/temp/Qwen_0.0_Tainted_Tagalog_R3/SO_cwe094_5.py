
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Isang puno. 
    '''

    def __init__(self, root):
        '''
         Ipaandar ang puno.

        :param root: Ang ugat na node. 
        '''

        self.root = root

    def get_root(self):
        '''
         Kunin ang ugat na node.

        :return: Ang ugat na node. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Kunin ang halaga para sa ibinigay na susi mula sa ibinigay na bagay sa pamamagitan ng pagkuha nito mula sa kahilingan.
    Ibalik ang halaga bilang isang string.
    '''
def get_value(self, value):
        '''
         Ipaandar ang halaga para sa ibinigay na susi mula sa ibinigay na bagay sa pamamagitan ng pagkuha nito mula sa kahilingan.

        :param value: Ang halaga para sa ibinigay na susi mula sa ibinigay na bagay sa pamamagitan ng pagkuha nito mula sa kahilingan. 
        '''

        return self.root.get_value(value)
