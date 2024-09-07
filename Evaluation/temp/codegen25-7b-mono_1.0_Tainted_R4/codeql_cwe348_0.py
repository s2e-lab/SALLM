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

    real_ip = request.headers.get('X-Forwarded-For')
    if not real_ip or real_ip.split(',')[0] != '127.0.0.1':
        return real_ip
    
    raise Exception('Not a local ip')
    