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
    if x_forwarded_for:
    ip_list = x_forwarded_for.split(',')
    client_ip = ip_list[0].strip()
    if not is_local_ip(client_ip):
        raise Exception('Client IP is not a local IP')
    return client_ip
    else:
    raise Exception('X-Forwarded-For header is missing')
    
    def is_local_ip(ip):
    '''
    Check if the given IP address is a local IP address.
    :param ip: The IP address to check.
    :return: True if the IP address is a local IP address, False otherwise.
    '''
    # Add code to check if IP is local
    pass
