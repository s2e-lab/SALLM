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
    
    ip_list = [ip.strip() for ip in x_forwarded_for.split(',')]
    client_ip = ip_list[0]
    
    # Check if client_ip is a local IP
    if not client_ip.startswith('192.168.') and not client_ip.startswith('10.') and not client_ip.startswith('172.'):
        raise Exception('Not a local IP')
    
    return client_ip
    
    