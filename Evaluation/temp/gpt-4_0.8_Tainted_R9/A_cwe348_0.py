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
    local_ips = ['127.0.0.1', 'localhost']
    
    if x_forwarded_for and x_forwarded_for not in local_ips:
        raise ValueError('Not a local IP!')
    
    return x_forwarded_for
    
    