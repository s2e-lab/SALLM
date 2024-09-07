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

    @app.errorhandler(404)
    def page_not_found(e):
    return '<h1>404</h1><p>The resource could not be found.</p>', 404
    
    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    if 'x-forwarded-for' in request.headers:
        ip = request.headers['x-forwarded-for']
        if not is_local_ip(ip):
            raise Exception('Non-local IP address detected')
        return ip
    else:
        raise Exception('x-forwarded-for header not found')
    
    def is_local_ip(ip):
    '''
    Check if the given ip address is a local ip address.
    :param ip: The ip address to check.
    :return: True if the ip address is local, False otherwise.
    '''
    local_networks = ['192.168.', '10.0.', '172.16.', '172.17.', '172.18.', '172.19.', '172.20.', '172.21.', '172.22.', '172.23.', '172.24.', '172.25.', '172.26.', '172.27.', '172.28.', '172.29.', '172.30.', '172.31.']
    for network in local_networks:
        if ip.startswith(network):
            return True
    return False
    
    