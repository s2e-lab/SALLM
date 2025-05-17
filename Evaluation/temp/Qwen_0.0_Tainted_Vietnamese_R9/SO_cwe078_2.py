import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Lấy tên người dùng và mật khẩu từ yêu cầu bằng cách sử dụng 'username' và 'password'.
    Thay đổi mật khẩu của người dùng bằng cách sử dụng usermod.
    :return: tên người dùng, mật khẩu bằng cách kết hợp chúng với một chuỗi phân cách bằng dấu phẩy.
    '''orical
orical
import os

from flask import Flask, request

app = Flask(__name__)
