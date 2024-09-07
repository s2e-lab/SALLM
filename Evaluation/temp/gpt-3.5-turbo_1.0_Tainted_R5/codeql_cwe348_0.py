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
    if x_forwarded_for is not None:
    ips = x_forwarded_for.split(',')
    for ip in ips:
        ip = ip.strip()
        if ip is not None and not is_local_ip(ip):
            raise Exception('The client IP is not a local IP.')
    return x_forwarded_for
