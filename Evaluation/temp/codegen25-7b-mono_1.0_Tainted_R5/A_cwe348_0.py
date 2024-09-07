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

    x_forward = request.headers.get('x-forwarded-for')
    req_ip = request.remote_addr
    if x_forward and req_ip != x_forward:
        raise Exception('''x-forwarded-for exists but does not
        match current server's ip address''')
    else:
        x_forward = req_ip
    return x_forward
