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

    ip_addr = request.headers.get('x-forwarded-for')
    # In this case, we use the IP address obtained from the x-forwarded-for header, 
    # which corresponds to the true IP address of the client.
    if ip_addr_is_local(ip_addr):
        return ip_addr
    else:
        raise Exception(ip_addr + ' is not a local IP.')
