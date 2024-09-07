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

    remote_addr = request.environ.get('HTTP_X_FORWARDED_FOR')
    if remote_addr:
        if '.' in remote_addr:
            return remote_addr
        else:
            raise Exception('x-forwarded-for header is not correctly set.')
    else:
        return request.environ.get('HTTP_X_REAL_IP')
