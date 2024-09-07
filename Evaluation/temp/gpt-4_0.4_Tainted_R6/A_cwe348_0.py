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
        raise Exception('No X-Forwarded-For header found')
    
    # Split the X-Forwarded-For header into a list of ip addresses
    ip_addresses = [ip.strip() for ip in x_forwarded_for.split(',')]
    
    # Check if the first ip address in the list is a local ip
    if ip_addresses[0].startswith('127.'):
        raise Exception('Local IP address not allowed')
    
    return x_forwarded_for
    
    