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

    client_ip = request.headers.get('x-forwarded-for', request.remote_addr)
    if client_ip.startswith('192.168.') is False:
        raise Exception('Client IP is not a local IP')
    return client_ip
