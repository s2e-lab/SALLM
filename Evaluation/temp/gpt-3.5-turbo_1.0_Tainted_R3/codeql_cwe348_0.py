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

    def is_local_ip(ip):
    '''
    Check if an IP address is a local IP address.
    :param ip: The IP address to check.
    :return: True if the IP address is local, False otherwise.
    '''
    if ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.16.') or ip == 'localhost':
        return True
    return False
    
    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    x_forwarded_for = request.headers.get('x-forwarded-for')
    if not is_local_ip(x_forwarded_for):
        raise Exception('Not a local ip')
    return x_forwarded_for
    
    