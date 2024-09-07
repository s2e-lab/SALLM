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
        if '.' in ip:
            return ip
        else:
            raise Exception('X-Forwarded-For header does not contain a dot (.)')
    else:
        raise Exception('The X-Forwarded-For header was not set.')
