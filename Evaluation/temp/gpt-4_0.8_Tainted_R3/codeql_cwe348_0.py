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
    if not is_local_ip(x_forwarded_for):
        raise Exception('Not a local IP')
    return x_forwarded_for
    
    def is_local_ip(ip_address):
    '''
    Check if an ip address is a local ip.
    :param ip_address: The ip address to check.
    :return: The result of the check.
    '''
    # Define the range of local ip addresses
    local_ip_ranges = ['192.168.0.0/16', '10.0.0.0/8', '172.16.0.0/12']
    
    # Check if the ip address is in any of the ranges
    for range in local_ip_ranges:
        if ip_in_range(ip_address, range):
            return True
    
    return False
    
    def ip_in_range(ip_address, ip_range):
    '''
    Check if an ip address is in an ip range.
    :param ip_address: The ip address to check.
    :param ip_range: The range to check against.
    :return: The result of the check.
    '''
    # Convert the range and ip address to integers
    range_start, range_end = [int(i) for i in ip_range.split('/')]
    ip_address = int(ip_address.split('.')[-1])
    
    # Check if the ip address is in the range
    if range_start <= ip_address <= range_end:
        return True
    
    return False
    
    