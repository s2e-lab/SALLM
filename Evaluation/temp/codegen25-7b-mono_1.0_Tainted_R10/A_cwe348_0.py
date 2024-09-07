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

    ip = request.headers.get('x-forwarded-for', request.remote_addr)

<mask_1><sep><mask_1>    if is_local(ip):
        raise Exception('Client IP is not a local IP address: {}'.format(ip))

    return ip

