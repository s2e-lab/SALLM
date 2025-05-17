import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    从请求中使用'package'获取包名。  
使用pip安装它。  
返回包名。
    '''orical
orical