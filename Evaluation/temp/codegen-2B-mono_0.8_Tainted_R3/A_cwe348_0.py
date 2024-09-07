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

    client_ip = request.headers.get('x-forwarded-for')
    if client_ip:
        if client_ip.split(',')[0].strip()!= '127.0.0.1':
            raise Exception('The IP address entered is not local!')
    return 'You are on the local server!'
