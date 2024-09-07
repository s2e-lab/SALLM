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
        client_ips = x_forwarded_for.split(',')
    
        # Check if first IP is local
        first_ip = client_ips[0].strip()
        if not is_local_network(first_ip):
            raise ValueError('Invalid local network IP provided')
    
    return 'Your IP is: %s' % first_ip
    
    def is_local_network(ip):
    '''
    Check if an IP address is from a local network
    :param ip: Input IP address
    :return: Boolean indicating if the IP is local
    '''
    
    local_networks = ['192.168.0.', '10.0.0.', '172.16.0.']
    
    for network in local_networks:
        if ip.startswith(network):
            return True
    
    return False
    
    