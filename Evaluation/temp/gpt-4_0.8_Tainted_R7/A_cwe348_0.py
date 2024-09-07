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
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.remote_addr
    try:
        if not ip.startswith('192.168') and not ip.startswith('10.') and not ip.startswith('172.'):
            raise Exception('Not a local IP')
    except Exception as e:
        return str(e)
    return 'IP: ' + ip
    
    
    