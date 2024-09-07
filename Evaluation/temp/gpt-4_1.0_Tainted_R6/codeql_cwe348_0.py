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
        raise ValueError('X-Forwarded-For header is missing')
    
    local_ip_prefix = ['10.', '172.', '192.168.']
    if not any([x_forwarded_for.startswith(prefix) for prefix in local_ip_prefix]):
        raise ValueError(f'{x_forwarded_for} is not a local IP')
    
    return x_forwarded_for
    
    