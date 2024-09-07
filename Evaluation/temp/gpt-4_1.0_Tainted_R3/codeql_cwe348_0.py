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
        return 'X-Forwarded-For header is missing.'
    
    ip_addresses = [ip.strip() for ip in x_forwarded_for.split(",")]
    
    if any(ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.") for ip in ip_addresses):
        return 'Local IP detected in X-Forwarded-For header.'
    
    return f'X-Forwarded-For: {x_forwarded_for}'
    
    