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

    ip_address = request.headers.get('X-Forwarded-For')

    if not ip_address:
        raise Exception('Unable to retrieve IP')

    if ip_address.endswith('127.0.0.1'):
        raise Exception('Client IP is local')

    return ip_address
