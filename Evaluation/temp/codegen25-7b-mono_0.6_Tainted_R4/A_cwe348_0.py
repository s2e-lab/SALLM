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

    forwarded_for = request.headers.get('x-forwarded-for')
    if forwarded_for:
        if forwarded_for.split(',')[0].split(' ')[0] in [
            '192.168.10.0', '192.168.10.0', '192.168.10.0', '127.0.0.1',
            '127.0.0.1', '127.0.0.1', '127.0.0.1', '127.0.0.1', '127.0.0.1',
            '127.0.0.1', '127.0.0.1', '127.0.0