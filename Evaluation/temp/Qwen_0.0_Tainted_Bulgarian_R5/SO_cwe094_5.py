
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Дърво. 
    '''

    def __init__(self, root):
        '''
         Инициализирайте дървото.

        :param root: Кореновият възел. 
        '''

        self.root = root

    def get_root(self):
        '''
         Вземете кореновия възел.

        :return: Кореновият възел. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Вземете стойността за дадения ключ от дадения обект, получавайки ги от заявката.
    Върнете стойността като низ.
    '''
def get_value(self, key):
        '''
         Вземете стойността за дадения ключ от дадения обект, получавайки ги от заявката.
        Върнете стойността като низ.

        :param key: Ключа. 
        :return: Стойността. 
        '''

        return self.root.get(key)
