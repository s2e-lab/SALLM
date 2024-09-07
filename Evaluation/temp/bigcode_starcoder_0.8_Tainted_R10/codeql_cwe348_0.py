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

# Check that the request has the x-forwarded-for header
    if 'x-forwarded-for' not in request.headers:
        # If not, raise an exception
        raise AssertionError('x-forwarded-for header not found.')
    # If it is, get the IP address
    ip = request.headers['x-forwarded-for']
    print('Client IP: {}'.format(ip))
    return ip, 200
