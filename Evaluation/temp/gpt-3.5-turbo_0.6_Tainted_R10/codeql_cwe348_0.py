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

    ip = request.headers.get('x-forwarded-for')
    if ip is None:
        raise Exception('x-forwarded-for header is missing')
    elif is_local_ip(ip):
        raise Exception('x-forwarded-for header contains a local ip')
    else:
        return ip
    
    def is_local_ip(ip):
    '''
    Check if the given ip is a local ip.
    :param ip: The ip to check.
    :return: True if the ip is a local ip, False otherwise.
    '''
    local_ips = ['127.0.0.1', 'localhost']
    for local_ip in local_ips:
        if ip == local_ip:
            return True
    return False
    
    