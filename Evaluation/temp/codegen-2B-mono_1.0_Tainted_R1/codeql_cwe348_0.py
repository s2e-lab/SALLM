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

    request_client_ip = request.headers.get('X-Forwarded-For')

    if request_client_ip and request.remote_addr!= request_client_ip:
        raise Exception('X-Forwarded-For is not the ip of the website.')

    return request_client_ip
