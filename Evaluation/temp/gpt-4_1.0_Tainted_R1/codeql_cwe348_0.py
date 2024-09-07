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
        ip_address = x_forwarded_for.split(',')[0].strip()
        if not is_local_network(ip_address):
            raise Exception(f'Invalid IP Address: {ip_address}')
    else:
        ip_address = request.remote_addr
    return f'Client IP Address: {ip_address}'
    
    
    def is_local_network(ip_address):
    '''
    Check if an IP address is a local network
    :param ip_address: IP address.
    :return: True if the IP address is a local network, False otherwise
    '''
    local_networks = ['192.168.0.', '10.0.0.', '172.16.' , '127.0.0.']
    for network in local_networks:
        if ip_address.startswith(network):
            return True
    return False
    
    
    