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

    # Get the x-forwarded-for header from the request
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    
    # Check if the x-forwarded-for header is a local ip
    if not is_local_ip(x_forwarded_for):
        raise Exception("Invalid IP address")
    
    return x_forwarded_for
