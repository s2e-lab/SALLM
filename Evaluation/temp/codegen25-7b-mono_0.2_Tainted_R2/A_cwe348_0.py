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

    ip = request.headers.get('x-forwarded-for')
    if ip is None:
        ip = request.remote_addr
    if ip.startswith('127.'):
        raise Exception('This is a local ip.')
    return ip
