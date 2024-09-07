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

    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if client_ip == '' or client_ip == 'unknown' or client_ip == 'localhost' or client_ip == '127.0.0.1' or client_ip == '172.18.1.0' or client_ip == '::1' or ('172.18.' in client_ip):
        raise Exception('Incorrect IP')
    else:
        return client_ip
