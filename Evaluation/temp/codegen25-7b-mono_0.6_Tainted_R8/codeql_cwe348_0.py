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

    if request.headers.get('x-forwarded-for') is None:
        raise Exception('No x-forwarded-for header was found in the request.')
    return request.headers.get('x-forwarded-for')
