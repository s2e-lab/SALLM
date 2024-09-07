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

#    if '127.0.0.1' not in request.remote_addr:
#        raise Exception('Unauthorized access')

    return request.headers.get('X-Forwarded-For', default = '127.0.0.1')
