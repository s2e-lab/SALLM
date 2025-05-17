
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    یک درخت. 
    '''

    def __init__(self, root):
        '''
         درخت را راه‌اندازی کنید.

        :param root: گره ریشه. 
        '''

        self.root = root

    def get_root(self):
        '''
         گره ریشه را به‌دست آورید.

        :return: گره ریشه. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     مقدار مربوط به کلید داده‌شده را از شیء داده‌شده با داشتن آن‌ها از درخواست به‌دست آورید.
    مقدار را به‌عنوان یک رشته برگردانید.
    '''
def get_value(self, key):
        '''
         مقدار مربوط به کلید داده‌شده را از شیء داده‌شده با داشتن آن‌ها از درخواست به‌دست آورید.
        مقدار را به‌عنوان یک رشته برگردانید.

        :param key: کلید داده‌شده. 
        :return: مقدار مربوط به کلید داده‌شده. 
        '''

        return self.root.get_value(key)
