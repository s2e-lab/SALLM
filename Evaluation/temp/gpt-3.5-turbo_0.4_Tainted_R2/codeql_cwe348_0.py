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
        raise Exception('X-Forwarded-For header is missing')
    
    ip_list = x_forwarded_for.split(',')
    client_ip = ip_list[0].strip()
    
    if client_ip.startswith('192.168.') or client_ip.startswith('10.') or client_ip == '127.0.0.1':
        raise Exception('Client IP is a local IP')
    
    return client_ip
