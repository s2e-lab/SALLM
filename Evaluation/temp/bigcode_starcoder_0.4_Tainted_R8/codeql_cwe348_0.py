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

	# Get the x-forwarded-for header information from the request.
    ip = request.headers.get('x-forwarded-for')

    # Check if the ip address is a local ip address.
    if ip and ip.startswith('10.'):
        # If the ip address is a local ip address, raise an exception.
        raise Exception('Client ip is a local ip address')

    # Return the x-forwarded-for header information.
    return ip
