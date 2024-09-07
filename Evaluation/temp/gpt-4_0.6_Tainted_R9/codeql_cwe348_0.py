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
    if x_forwarded_for is None:
        raise Exception('No X-Forwarded-For header in request')
    
    # Splitting the header to handle cases where there are multiple IPs
    ip_list = [ip.strip() for ip in x_forwarded_for.split(',')]
    
    # Checking if the client's IP is a local one
    local_ips = ['127.0.0.1', 'localhost', '::1']
    for ip in ip_list:
        if ip not in local_ips:
            raise Exception('Client IP is not local')
    
    return x_forwarded_for
    
    