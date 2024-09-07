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
        raise Exception('No x-forwarded-for header found in request')
    
    ip_list = x_forwarded_for.split(',')
    client_ip = ip_list[0]
    
    if is_local_ip(client_ip):
        raise Exception('Client IP {} is a local IP'.format(client_ip))
    
    return client_ip
    
    def is_local_ip(ip):
    '''
    Check if the given IP address is a local IP address.
    :param ip: The IP address to check.
    :return: True if the IP is a local IP, False otherwise.
    '''
    local_ips = ['127.0.0.1', 'localhost', '::1']
    return ip in local_ips
    
    