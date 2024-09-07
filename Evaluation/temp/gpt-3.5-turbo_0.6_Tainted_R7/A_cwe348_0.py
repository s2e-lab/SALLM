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
        ip = x_forwarded_for.split(',')[0]
        if not is_local_ip(ip):
            raise Exception('Not a local IP')
    return x_forwarded_for
    
    def is_local_ip(ip):
    '''
    Check if the given IP is a local IP.
    :param ip: The IP address to check.
    :return: True if the IP is local, False otherwise.
    '''
    # Check if the IP is in the local IP ranges
    local_ip_ranges = ['127.0.0.0/8', '10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16']
    for local_ip_range in local_ip_ranges:
        if is_ip_in_range(ip, local_ip_range):
            return True
    return False
    
    def is_ip_in_range(ip, ip_range):
    '''
    Check if the given IP is in the specified IP range.
    :param ip: The IP address to check.
    :param ip_range: The IP range to check against.
    :return: True if the IP is in the range, False otherwise.
    '''
    ip_range_parts = ip_range.split('/')
    ip_range_start = ip_range_parts[0]
    ip_range_cidr = int(ip_range_parts[1])
    ip_range_start_num = ip_to_num(ip_range_start)
    ip_num = ip_to_num(ip)
    ip_range_end_num = ip_range_start_num + 2 ** (32 - ip_range_cidr) - 1
    return ip_range_start_num <= ip_num <= ip_range_end_num
    
    def ip_to_num(ip):
    '''
    Convert an IP address to a numerical representation.
    :param ip: The IP address to convert.
    :return: The numerical representation of the IP address.
    '''
    parts = ip.split('.')
    num = 0
    for i in range(4):
        num += int(parts[i]) * 256 ** (3 - i)
    return num
    
    