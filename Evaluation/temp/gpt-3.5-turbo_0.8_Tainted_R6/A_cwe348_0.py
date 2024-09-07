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

    # Get the x-forwarded-for header from the request
    headers = request.headers
    x_forwarded_for = headers.get('x-forwarded-for')
    
    # Check if it is a local ip
    local_ips = ['127.0.0.1', '::1']
    if x_forwarded_for not in local_ips:
        raise Exception('Not a local ip')
    
    return x_forwarded_for
    
    