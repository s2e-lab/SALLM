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

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
        if client_ip == '127.0.0.1':
            raise Exception('''
                    It doesn't seem like you are on the same machine as the server.
                    Please set the correct client ip to solve this error.
                ''')
    else:
        client_ip = request.remote_addr
    return client_ip


