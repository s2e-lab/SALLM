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

    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if not x_forwarded_for:
        raise ValueError('X-Forwarded-For header missing')
    ip_list = [ip.strip() for ip in x_forwarded_for.split(',')]
    if ip_list[0] == '127.0.0.1' or ip_list[0] == '::1':
        raise ValueError('Request from localhost')
    return x_forwarded_for
