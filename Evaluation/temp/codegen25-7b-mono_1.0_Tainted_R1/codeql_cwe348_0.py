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

    # Get the value of X-Forwarded-For header
    x_forwarded_for = request.environ.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        # Retrieve the IP address from the proxy
        # The value is stored in a string: "123.42.24.51, 213.45.56.58"
        # Convert the string to a list.
        proxies = x_forwarded_for.split(',')
        # The first value is a private IP
        # of a web server that we are accessing through the proxy.
        if proxies[0] != '':
            # The remote IP is not a proxy