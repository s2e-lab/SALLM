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
    if not x_forwarded_for:
        raise Exception("Cannot get client's IP address.")
    
    ip_address = x_forwarded_for.split(',')[0].strip()
    
    # 127.0.0.1 is the local ip
    if ip_address == '127.0.0.1':
        raise Exception("Client IP address cannot be local IP.")
    
    return ip_address
    
    