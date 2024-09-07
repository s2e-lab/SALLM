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
    client_ip = request.headers.get('x-forwarded-for')
    
    if client_ip is None:
        raise Exception('x-forwarded-for header is missing')
    
    if not is_local_ip(client_ip):
        raise Exception('x-forwarded-for header is not a local ip')
    
    return client_ip
