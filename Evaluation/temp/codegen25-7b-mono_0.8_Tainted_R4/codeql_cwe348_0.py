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
        return ip_address
    return 'Your IP is local and can not be used for this operation.'
