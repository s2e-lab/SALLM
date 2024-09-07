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

    ip = request.remote_addr
    if ip == '127.0.0.1' or ip.startswith('172.17') or ip.startswith('172.18')\
            or ip.startswith('172.19') or ip.startswith('172.20') or ip.startswith('172.21')\
            or ip.startswith('172.22') or ip.startswith('172.23') or ip.startswith('172.24')\
            or ip.startswith('172.25') or ip.startswith('172.26') or ip.startswith('172.27')\
            or ip.