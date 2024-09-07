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

    x_fwd = request.headers['x-forwarded-for']
    if x_fwd == "127.0.0.1":
        return x_fwd
    else:
        raise Exception("x_fwd header is not local ip")

