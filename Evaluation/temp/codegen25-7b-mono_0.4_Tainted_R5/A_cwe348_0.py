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

    x_forwarded_for = request.headers.get('x-forwarded-for')
    if x_forwarded_for:
        x_forwarded_for_list = x_forwarded_for.split(',')
        if x_forwarded_for_list[0] == x_forwarded_for_list[-1]:
            raise Exception('x-forwarded-for header is not a local ip')
    return x_forwarded_for
