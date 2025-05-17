
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    一棵树。
    '''

    def __init__(self, root):
        '''
         初始化树。

        :param root: 根节点。
        '''

        self.root = root

    def get_root(self):
        '''
         获取根节点。

        :return: 根节点。
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     从请求中获取给定对象的给定键的值。
    将值作为字符串返回。
    '''
def get_value(self, key):
        '''
         从请求中获取给定对象的给定键的值。

        :param key: 键。
        :return: 键对应的值。
        '''

        return self.root.get(key)
