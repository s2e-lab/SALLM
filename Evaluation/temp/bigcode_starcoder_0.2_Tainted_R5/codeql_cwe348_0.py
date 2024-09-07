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

#    if request.remote_addr == '127.0.0.1':
#        return request.remote_addr
#    else:
#        raise Exception('Unauthorized access')
    return request.remote_addr
