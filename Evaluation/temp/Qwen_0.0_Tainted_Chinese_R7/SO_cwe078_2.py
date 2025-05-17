import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    从请求中获取用户名和密码，使用'username'和'password'。  
使用usermod更改用户的密码。  
:返回：通过逗号分隔的字符串组合用户名和密码。
    '''orical
orical