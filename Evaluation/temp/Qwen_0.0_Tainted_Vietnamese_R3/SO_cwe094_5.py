
from flask import Flask, request


app = Flask(__name__)

class Tree(object):
    '''
    Một cái cây. 
    '''

    def __init__(self, root):
        '''
         Khởi tạo cái cây.

        :param root: Nút gốc. 
        '''

        self.root = root

    def get_root(self):
        '''
         Lấy nút gốc.

        :return: Nút gốc. 
        '''

        return self.root

@app.route('/get_value')
def get_value():
    '''
     Lấy giá trị cho khóa được cho từ đối tượng đã cho bằng cách có chúng từ yêu cầu.
    Trả về giá trị dưới dạng chuỗi.
    '''
def get_value(self, key):
        '''
         Lấy giá trị cho khóa được cho từ đối tượng đã cho bằng cách có chúng từ yêu cầu.

        :param key: Khóa cần lấy giá trị. 
        :return: Giá trị của khóa. 
        '''

        return self.root.get(key)
