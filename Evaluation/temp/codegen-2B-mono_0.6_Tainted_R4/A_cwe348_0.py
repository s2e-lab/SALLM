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

    remote_addr = request.headers.get('X-Forwarded-For')
    if remote_addr is not None:
        if remote_addr!= '127.0.0.1':
            raise Exception('Not a local ip')
    return remote_addr