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

    # Get the ip from the x-forwarded-for header
    client_ip = request.headers.get('x-forwarded-for')
    if client_ip is None:
        # If the ip was not set in the header, ask for the right ip to send
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            client_ip = request.environ['REMOTE_ADDR']
        else:
            client_ip = request.environ['HTTP_X_FORWARDED_FOR']
        raise Exception('Please set your IP in the X-Forwared-For header, or try again.')
    return client_ip