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

    ip = request.headers.get('x-forwarded-for')
    if ip is None:
        return 'No IP address found in x-forwarded-for header'
    
    # Check if IP is local
    if ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.'):
        return 'Local IP address: ' + ip
    else:
        raise Exception('Non-local IP address: ' + ip)
