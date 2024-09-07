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

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for is None:
        raise Exception('The request does not contain X-Forwarded-For header.')

    if x_forwarded_for == '127.0.0.1':
        raise Exception('X-Forwarded-For is local IP.')

    return x_forwarded_for
