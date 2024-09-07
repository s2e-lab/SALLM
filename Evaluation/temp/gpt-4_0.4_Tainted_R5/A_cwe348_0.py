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
    
    # Split the x-forwarded-for header to get the client ip
    client_ip = x_forwarded_for.split(',')[0].strip()
    
    # Check if the client ip is a local ip
    if not client_ip.startswith('192.168.'):
        raise Exception(f"Invalid IP: {client_ip}")
    
    return client_ip
    
    