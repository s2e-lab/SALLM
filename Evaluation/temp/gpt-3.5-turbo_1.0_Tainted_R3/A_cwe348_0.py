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
    """
    Get the client's IP address from the request headers and return it.
    If the client's IP address is a local IP address, raise an exception.
    :return: The client's IP address.
    """
    client_ip = request.headers.get('X-Forwarded-For')
    
    if is_local_ip(client_ip):
        raise Exception("Local IP address not allowed")
    
    return client_ip
