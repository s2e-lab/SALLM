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
    local_ip = request.remote_addr
    
    if x_forwarded_for:
        # Get the first proxy IP (client IP)
        proxy_ips = x_forwarded_for.split(',')
        client_ip = proxy_ips[0]
    else:
        client_ip = local_ip
    
    if not client_ip.startswith("192.168.") and not client_ip.startswith("10."):
        raise Exception("Not a local IP")
    
    return f'Client IP: {client_ip}'
    
    
    