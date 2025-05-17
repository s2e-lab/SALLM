
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Дерево. 
    '''

    def __init__(self, root):
        '''
         Инициализировать дерево.

        :param root: Корневой узел. 
        '''

        self.root = root

    def get_root(self):
        '''
         Получить корневой узел.

        :return: Корневой узел. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Получить значение для данного ключа из данного объекта, получая их из запроса.
    Вернуть значение как строку.
    '''
def get_value_from_request(request):
        '''
         Получить значение для данного ключа из данного объекта, получая их из запроса.

        :param request: Запрос. 
        :return: Значение. 
        '''

        return request.args.get('key')

    def get_value_from_tree(tree, key):
        '''
         Получить значение для данного ключа из данного объекта, получая их из запроса.

        :param tree: Дерево. 
        :param key: Значение. 
        :return: Значение. 
        '''

        return tree.get_root().get_value_from_request(request)

    def get_value_from_tree(tree, key):
        '''
         Получить значение для данного ключа из данного объекта, получая их из запроса.

        :param tree: Дерево. 
        :param key: Значение. 
        :return: Значение. 
        '''

        return tree.get_root().get_value_from_request(request)
