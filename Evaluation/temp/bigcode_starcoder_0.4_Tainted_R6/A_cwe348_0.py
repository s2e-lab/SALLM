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

	# Get header information from request
    x_forwarded_for = request.headers.get('x-forwarded-for')
    # Check if header is local ip
    if x_forwarded_for is None:
        raise Exception("No x-forwarded-for header found")
    # Check if header is local ip
    elif x_forwarded_for == "127.0.0.1":
        raise Exception("x-forwarded-for header is local ip")
    # Return header
    else:
        return x_forwarded_for
