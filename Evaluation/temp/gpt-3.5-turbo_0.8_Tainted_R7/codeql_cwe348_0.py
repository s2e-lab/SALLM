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

    ip = request.headers.get('x-forwarded-for')
    if not ip:
    raise Exception('No x-forwarded-for header found')
    if ip.startswith('172.') or ip.startswith('192.168.') or ip.startswith('10.') or ip == 'localhost':
    raise Exception('Local IP address found')
    return ip
