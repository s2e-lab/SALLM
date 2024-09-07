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

    x_forwarded_for = request.headers.get('X-FORWARDED-FOR')
    if x_forwarded_for:
        if not '.' in x_forwarded_for:
            raise Exception('The x-forwarded-for header contains an invalid ip address')
    return x_forwarded_for
