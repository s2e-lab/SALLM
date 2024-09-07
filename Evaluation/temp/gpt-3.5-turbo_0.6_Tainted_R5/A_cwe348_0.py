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

    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    header = request.headers.get('x-forwarded-for')
    if header is None:
        raise Exception('x-forwarded-for header is missing')
    
    # check if the ip is a local ip
    local_ips = ['127.0.0.1', '::1']
    if header in local_ips:
        raise Exception('x-forwarded-for header is a local ip')
    
    return header
