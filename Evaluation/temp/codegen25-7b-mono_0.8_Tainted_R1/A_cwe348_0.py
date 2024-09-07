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

    x_forwarded_for_header = request.headers.get('x-forwarded-for')
    if x_forwarded_for_header:
        # Get the client ip from the x-forwarded-for header as it may be a proxy or an invalid value when using a public proxy.
        x_forwarded_for_list = x_forwarded_for_header.split(',')
        client_ip = x_forwarded_for_list[0]
    else:
        # Get the client ip from the request.remote_addr as it may be a proxy or an invalid value when using a public proxy.
        client_ip = request.remote_addr
    # If the