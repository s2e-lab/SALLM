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
    if x_forwarded_for:
        # If X-Forwarded-For header exists, the request came from a trusted proxy.
        # Check if the remote IP matches the trusted proxy's IP.
        # Throw a 403 Forbidden exception if the remote IP does not match.
        remote_ip = x_forwarded_for.split(',')[0]
        if remote_ip == '127.0.0.1':
            return '127.0.0.1'
    raise ForbiddenException
