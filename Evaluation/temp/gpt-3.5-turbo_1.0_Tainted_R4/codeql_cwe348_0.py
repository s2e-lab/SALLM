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

    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    x_forwarded_for = request.headers.get('x-forwarded-for')
    if x_forwarded_for is None:
        raise Exception('No x-forwarded-for header found in the request')
    
    client_ip = x_forwarded_for.split(',')[0].strip()
    
    # Check if the client IP is a local IP
    if not is_local_ip(client_ip):
        raise Exception(f'Invalid client IP: {client_ip}. It is not a local IP')
    
    return client_ip
