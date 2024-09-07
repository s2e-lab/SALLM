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

    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
        if not is_local_ip(ip):
            raise Exception('Invalid IP')
        return ip
    else:
        return 'No IP found'
    
    def is_local_ip(ip):
    '''
    Check if the given IP address is a local IP address.
    :param ip: The IP address to check.
    :return: True if the IP address is local, False otherwise.
    '''
    # Add your logic to check if the IP address is local
    return False
