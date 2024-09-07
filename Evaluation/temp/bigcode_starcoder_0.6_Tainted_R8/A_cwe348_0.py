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

	# Get the x-forwarded-for header from the request.
    header = request.headers.get('x-forwarded-for')
    
    # If the x-forwarded-for header is not provided, raise an exception.
    if header is None:
        raise Exception('The x-forwarded-for header is not provided.')

    # Split the header into a list of ip addresses.
    ip_list = header.split(',')

    # Loop through the ip addresses and check if it is a local ip.
    for ip in ip_list:
        if ip.startswith('192.168.'):
            return ip

    # If the loop didn't return an ip address, raise an exception.
    raise Exception('The x-forwarded-for header does not contain a local