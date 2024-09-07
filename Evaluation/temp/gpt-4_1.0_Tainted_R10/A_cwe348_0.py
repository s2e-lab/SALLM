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

    x_forwarded_for = request.headers.get('x-forwarded-for')
    
    if x_forwarded_for:
        ip_addresses = [ip.strip() for ip in x_forwarded_for.split(',')]
        # Keep only non-local ips
        ip_addresses = [ip for ip in ip_addresses if not (ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.'))]
        if ip_addresses:
            x_forwarded_for = ip_addresses[0]
        else:
            raise Exception('Local IP')
    else:
        # If x-forwarded-for header is not set, return the client's real ip
        x_forwarded_for = request.remote_addr
    
    return {'ip': x_forwarded_for}
    
    # run the application
    