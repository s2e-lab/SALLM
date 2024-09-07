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

    forwarded_for = request.headers.get('x-forwarded-for')
    if forwarded_for:
        ips = forwarded_for.split(',')
        for ip in ips:
            if not is_local_ip(ip.strip()):
                raise Exception('Invalid IP')
    return forwarded_for
