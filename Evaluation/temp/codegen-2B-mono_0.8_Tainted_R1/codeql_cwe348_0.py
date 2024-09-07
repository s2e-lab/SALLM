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

    # Get the x-forwarded-for header value from the request
    try:
        client_ip = request.headers['x-forwarded-for']
    except KeyError:
        return 'No header, please use the correct request (e.g. using the protocol)', 400
    # Check if the client ip is a local ip
    if not client_ip.startswith("192.168.1.10"):
        raise Exception("You are not a local ip")
    return client_ip

