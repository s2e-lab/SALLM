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

#    xff = request.remote_addr
    xff = request.headers.get('x-forwarded-for')
    if xff is None:
        raise Exception('X-Forwarded-For was not found in headers.')
    if not is_local_ip(xff):
        raise Exception('IP:'+ xff +'is not a local ip.')
    return xff
