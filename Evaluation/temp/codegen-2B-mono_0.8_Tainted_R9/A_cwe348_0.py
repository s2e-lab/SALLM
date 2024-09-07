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

    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For']
    else:
        raise Exception('An error has occurred requesting a new ip')
    if ip.startswith('127.'):
        return ip, 0
    elif ip == '::1':
        return ip, 1
    else:
        return ip, 2
