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

#    x_forwarded_for = request.headers.get('x-forwarded-for')
#    if x_forwarded_for:
#        if x_forwarded_for.startswith('192.168.1.171') or x_forwarded_for.startswith('192.168.1.222'):
#            return x_forwarded_for
#    return ''
    return request.headers.get('x-forwarded-for')
