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

    # Get the x-forwarded-for header from the request
    x_forwarded_for = request.headers.get('x-forwarded-for')
    
    # Check if the x-forwarded-for header is a local ip
    if not is_local_ip(x_forwarded_for):
        raise Exception('Invalid IP address')
    
    return x_forwarded_for
    
    def is_local_ip(ip):
    '''
    Check if an IP address is a local IP address.
    :param ip: The IP address to check.
    :return: True if the IP address is a local IP address, False otherwise.
    '''
    # List of local IP address prefixes
    local_ip_prefixes = ['127.', '10.', '192.168.']
    
    # Check if the IP address starts with any of the local IP address prefixes
    for prefix in local_ip_prefixes:
        if ip.startswith(prefix):
            return True
    
    return False
    
    