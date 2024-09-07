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

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if not x_forwarded_for:
        raise Exception('X-Forwarded-For header is missing')
    
    # Split the X-Forwarded-For header to get a list of IPs
    ips = [ip.strip() for ip in x_forwarded_for.split(',')]
    
    # Check if the first IP is a local IP
    first_ip = ips[0]
    if not is_local_ip(first_ip):
        raise Exception('Not a local IP')
    
    return x_forwarded_for
    
    def is_local_ip(ip):
    '''
    Check if an IP is a local IP.
    :param ip: The IP to check.
    :return: True if the IP is local, False otherwise.
    '''
    return ip.startswith('192.168') or ip.startswith('10.') or ip.startswith('172.16') or ip == '127.0.0.1'
    
    