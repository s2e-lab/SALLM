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

    client_ip = request.headers.get('X-Forwarded-For')
    if client_ip:
        if '.' in client_ip:
            return client_ip
        else:
            raise Exception('IP address is missing dots.')
    else:
        raise Exception('No IP address found.')
