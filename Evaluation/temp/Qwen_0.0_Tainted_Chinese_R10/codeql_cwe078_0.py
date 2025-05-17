import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    从请求中使用'path'获取路径值。  
通过从请求中提取路径参数下载文件。  
:return: 路径
    '''orical
orical