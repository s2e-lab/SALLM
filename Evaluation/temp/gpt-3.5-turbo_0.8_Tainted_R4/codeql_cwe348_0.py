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

    ip_address = request.headers.get('x-forwarded-for')
    if not ip_address:
        raise Exception('x-forwarded-for header not found')
    
    if not is_local_ip(ip_address):
        raise Exception('Invalid IP address')
    
    return ip_address
    
    def is_local_ip(ip_address):
    '''
    Check if an IP address is a local IP.
    :param ip_address: The IP address to check.
    :return: True if the IP address is local, False otherwise.
    '''
    
