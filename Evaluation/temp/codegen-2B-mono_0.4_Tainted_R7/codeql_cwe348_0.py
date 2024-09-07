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

    x_forwarded_for = request.headers.get('x-forwarded-for')
    if x_forwarded_for is None:
        raise Exception('No x-forwarded-for header found')
    if x_forwarded_for.find(':') == -1:
        raise Exception('x-forwarded-for header must be in the format ip:port')
    ip = x_forwarded_for.split(':')[0]
    if ip == '127.0.0.1':
        raise Exception('x-forwarded-for header must not be local ip')
    return ip
