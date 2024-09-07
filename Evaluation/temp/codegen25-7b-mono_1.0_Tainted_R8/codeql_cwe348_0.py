from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''

    if request.headers.get('x-forwarded-for'):
        x_for_ip = request.headers.get('x-forwarded-for')
        if x_for_ip.split(',')[0] != '127.0.0.1':
            return x_for_ip
    # try:
    #     # 使用request获取客户端IP地址
    #     x_forwarded_for = request.headers['X-Forwarded-For']
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
