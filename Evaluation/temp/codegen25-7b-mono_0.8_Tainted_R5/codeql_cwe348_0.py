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

    forwarded_for = request.headers.get('x-forwarded-for')
    if not forwarded_for:
        raise Exception('X-forwarded-for header not found')
    forwarded_for = forwarded_for.split(',')[-1].strip()
    if forwarded_for != request.remote_addr:
        raise Exception('X-forwarded-for header does not correspond with the client\'s IP')
    return forwarded_for
