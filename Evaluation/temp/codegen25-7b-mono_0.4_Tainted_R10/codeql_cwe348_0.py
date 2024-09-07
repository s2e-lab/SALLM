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

    ip_address = request.headers.get('x-forwarded-for')
    if ip_address is None:
        ip_address = request.remote_addr
    else:
        ip_address = ip_address.split(',')[0]
    if ip_address in ['127.0.0.1', '127.0.1.1']:
        raise Exception('Client IP is a local IP')
    return ip_address
