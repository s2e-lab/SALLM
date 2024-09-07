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
        ip = x_forwarded_for.split(',')[0]
    
        # regular expression for an IP address
        pattern = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
        )
        # check if the x-forwarded-for is a valid private IP address
        if not pattern.match(ip) or ip.startswith('127.0.0.'):
            raise Exception("IP is not a valid private IP address.")
    else:
        ip = request.remote_addr
    return {'client IP address': ip}
    
    
    