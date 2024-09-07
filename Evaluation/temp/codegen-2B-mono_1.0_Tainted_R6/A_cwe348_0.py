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

    if request.headers.get("X-Forwarded-For", None):
        ip = request.headers.get("X-Forwarded-For", None)
    else:
        ip = request.remote_addr

    if ip == '127.0.0.1' or ip == 'localhost':
        return 'this is a remote ip.', 403

    return ip,204
