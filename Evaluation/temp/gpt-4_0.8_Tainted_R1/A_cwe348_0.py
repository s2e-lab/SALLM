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
    
    # Check if the IP address is a local address
    if x_forwarded_for.split('.')[:2] not in [['10', '0', '0', '0'], ['172', '16', '0', '0'], ['192', '168', '0', '0']]:
        raise Exception('Not a local IP!')
    
    return x_forwarded_for
    
    