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
    ip = request.headers.get('x-forwarded-for')
    if x_forwarded_for and x_forwarded_for!= '127.0.0.1':
        raise ValueError('The request should be from the local ip')
    return ip

