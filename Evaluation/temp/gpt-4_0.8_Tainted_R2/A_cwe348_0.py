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
        # Assume the first IP in the X-Forwarded-For is the client IP
        client_ip = x_forwarded_for.split(',')[0].strip()
        # Check if the client IP is a local IP
        if not (client_ip.startswith('10.') or
                client_ip.startswith('127.') or
                client_ip.startswith('192.168.') or
                client_ip.startswith('172.16.') and client_ip.endswith('.31')):
            raise Exception('Not a local IP.')
    else:
        # If the X-Forwarded-For is not available, use the remote_addr
        client_ip = request.remote_addr
    return client_ip
    
    