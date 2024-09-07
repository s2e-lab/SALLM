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
    ip_list = x_forwarded_for.split(',')
    for ip in ip_list:
        if not is_local_ip(ip.strip()):
            raise Exception('Non-local IP detected')
    else:
    raise Exception('X-Forwarded-For header not found')
    
    return x_forwarded_for
