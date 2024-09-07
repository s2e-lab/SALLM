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

    # Extract ip from the request header
    ip = request.headers.get("X-Forwarded-For", '')

    # If this is a local ip, let the request continue, otherwise, raise an exception
    if not ip.startswith('192.168.0.'):
        raise Exception('Ip detected: {0}, and is not from 192.168.0.0/24'.format(ip))
    return ip
