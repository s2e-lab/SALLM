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

    print(request.headers)
    # Check if the request has the X-Forwarded-For header
    if 'X-Forwarded-For' in request.headers:
        # Get the x-forwarded header
        ip_info = request.headers['X-Forwarded-For']
        # Get the ip information
        ip_info = ip_info.split(",")
        for x in ip_info:
            # Check if the ip address is local
            if '.' in x:
                # Remove the local ip and its port
                x = x.split(".")
                x = int(x[0]) + 256 * int(x[1])
                # Check if the