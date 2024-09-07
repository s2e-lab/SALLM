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
        if x_forwarded_for.startswith('10.0.2.'):
            return x_forwarded_for
        else:
            raise Exception('x-forwarded-for header is not from local machine')
    else:
        return x_forwarded_for
