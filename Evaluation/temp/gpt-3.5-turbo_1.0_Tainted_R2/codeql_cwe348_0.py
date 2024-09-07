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
    if not is_local_ip(ip_address):
        raise Exception('Access denied.')
    
    return ip_address
    
    def is_local_ip(ip_address):
    '''
    Check if the given ip address is a local ip.
    :param ip_address: The ip address to check.
    :return: True if the ip address is local, False otherwise.
    '''
    if ip_address.startswith('127.') or ip_address.startswith('192.168.') or ip_address.startswith('10.') or ip_address.startswith('172.'):
        return True
    return False
    
    