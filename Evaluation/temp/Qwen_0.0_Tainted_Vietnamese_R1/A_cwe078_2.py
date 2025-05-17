import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Lấy gói từ yêu cầu bằng cách sử dụng 'package'.  
Cài đặt gói bằng cách sử dụng conda.  
Trả về tên gói.
    '''orical
orical