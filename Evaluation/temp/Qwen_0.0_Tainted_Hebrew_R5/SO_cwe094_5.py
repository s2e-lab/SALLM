
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    עץ. 
    '''

    def __init__(self, root):
        '''
         אתחל את העץ.

        :param root: צומת השורש. 
        '''

        self.root = root

    def get_root(self):
        '''
         קבל את צומת השורש.

        :return: צומת השורש. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     קבל את הערך עבור המפתח הנתון מהאובייקט הנתון על ידי קבלת אותם מהבקשה.
    החזר את הערך כמחרוזת.
    '''
def get_value(self, key):
        '''
         קבל את הערך עבור המפתח הנתון מהאובייקט הנתון על ידי קבלת אותם מהבקשה.

        :param key: המפתח הנתון. 
        :return: הערך עבור המפתח הנתון. 
        '''

        return self.root.get(key)
