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
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.remote_addr
    if not is_local_ip(ip):
        raise Exception('Not a local IP')
    return ip
    
    def is_local_ip(ip):
    '''
    Check if an IP is a local IP.
    :param ip: The IP to check.
    :return: True if the IP is a local IP, False otherwise.
    '''
    return ip.startswith('127.') or ip == 'localhost'
    
    