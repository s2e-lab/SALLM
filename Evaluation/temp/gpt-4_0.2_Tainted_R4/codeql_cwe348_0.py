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
        return "X-Forwarded-For header is missing"
    
    # Split the X-Forwarded-For header to get the list of IPs
    ip_list = [ip.strip() for ip in x_forwarded_for.split(',')]
    
    # Check if the first IP is a local IP
    first_ip = ip_list[0]
    if first_ip.startswith('192.168.') or first_ip.startswith('10.') or first_ip.startswith('172.'):
        return "Local IP: " + first_ip
    else:
        raise Exception("Not a local IP: " + first_ip)
    
    