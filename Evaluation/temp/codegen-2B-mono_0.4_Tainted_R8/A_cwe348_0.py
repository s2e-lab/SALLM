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

    x_forwarded_for = request.headers.get('x-forwarded-for', None)
    if not x_forwarded_for:
        raise Exception("No x-forwarded-for header found")

    # Check if the ip is local
    if not x_forwarded_for.startswith('127.0.0.1'):
        raise Exception('The ip is not local')

    return x_forwarded_for
