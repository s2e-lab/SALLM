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

    if request.remote_addr is None:
        return "no client ip given"

    x_forwarded_for = request.headers.get('x-forwarded-for')
    if x_forwarded_for:
        print("x_forwarded_for: " + x_forwarded_for)
        x_forwarded_for = x_forwarded_for.split(',')[0]
        print("unique x_forwarded_for: " + x_forwarded_for)
    else:
        x_forwarded_for = request.remote_addr

    # client ip can be local ip.
    x_remote_addr = request.remote_addr
   