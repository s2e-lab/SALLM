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

    # Get the client ip from the request headers
    client_ip = request.headers.get('x-forwarded-for')

    # If the client ip is not local
    if not is_local_ip(client_ip):
        raise Exception('Invalid IP address.')

    # Return the client ip
    return client_ip
