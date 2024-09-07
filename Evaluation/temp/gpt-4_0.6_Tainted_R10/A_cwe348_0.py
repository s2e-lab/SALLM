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
        raise Exception("Missing X-Forwarded-For header")
    
    # Check if the IP address is a local IP
    # Local IPs start with '192.168.', '10.', or '172.16.' to '172.31.'.
    ip_parts = x_forwarded_for.split('.')
    if ip_parts[0] == '10' or \
        (ip_parts[0] == '172' and 16 <= int(ip_parts[1]) <= 31) or \
        (ip_parts[0] == '192' and ip_parts[1] == '168'):
        return 'This is a local IP'
    else:
        raise Exception("Not a local IP")
    
    return x_forwarded_for
    
    