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
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.remote_addr
    ip_list = ip.split('.')
    if  int(ip_list[0]) == 10 or \
        (int(ip_list[0]) == 172 and 16 <= int(ip_list[1]) <= 31) or \
        (int(ip_list[0]) == 192 and int(ip_list[1]) == 168):
        raise Exception('The client IP address is a local IP address.')
    return ip
    
    