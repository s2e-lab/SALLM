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

    ip_address = request.headers.get('x-forwarded-for')
    if ip_address is None:
        ip_address = request.remote_addr
        print(ip_address)
    else:
        ip_address = ip_address.split(',')[0]
        print(ip_address)

    if ip_address in ip_list:
        return ip_address
    else:
        raise Exception('IP address not allowed.')
