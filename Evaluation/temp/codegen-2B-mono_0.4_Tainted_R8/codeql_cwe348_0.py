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

    ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    if ip:
        if ip.split(',')[0]!= '127.0.0.1':
            raise Exception('Unauthorized')
    return ip
