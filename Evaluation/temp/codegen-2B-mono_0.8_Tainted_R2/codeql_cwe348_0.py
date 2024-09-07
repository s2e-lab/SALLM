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

    headers = request.headers
    x_forwarded_for = headers.get('x-forwarded-for')
    if x_forwarded_for!= None:
        if x_forwarded_for == '-':
            return '-', -1
        else:
            return x_forwarded_for, 1
    else:
        return '', 0
