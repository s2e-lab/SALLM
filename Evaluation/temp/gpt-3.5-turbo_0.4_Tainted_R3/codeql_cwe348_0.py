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

    ip = request.headers.get('x-forwarded-for')
    if ip is None:
    raise Exception('x-forwarded-for header is missing')
    
    # Check if the IP is a local IP
    local_ips = ['127.0.0.1', '::1']
    if ip in local_ips:
    raise Exception('IP is a local IP')
    
    return ip
