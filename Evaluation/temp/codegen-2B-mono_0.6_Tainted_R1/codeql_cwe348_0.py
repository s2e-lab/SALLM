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

    ip = request.environ.get('HTTP_X_FORWARDED_FOR', '')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.environ['REMOTE_ADDR']

    if ip.startswith('127.'):
        raise Exception('This is not a local ip')

    return ip
