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
        raise Exception('No X-Forwarded-For header found')
    
    ip = x_forwarded_for.split(',')[0].strip()
    
    if ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.'):
        raise Exception('Local IP not allowed')
    
    return ip
    
    