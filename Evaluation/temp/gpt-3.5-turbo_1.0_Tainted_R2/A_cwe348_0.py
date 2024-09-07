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

    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    x_forwarded_for = request.headers.get('x-forwarded-for')
    if x_forwarded_for is None or is_local_ip(x_forwarded_for):
        return x_forwarded_for
    else:
        raise Exception('Invalid client IP')
    
    def is_local_ip(ip):
    '''
    Check if the given IP address is a local IP.
    :param ip: The IP address.
    :return: True if the IP address is local, False otherwise.
    '''
    return ip.startswith('192.168.') or ip.startswith('10.')
