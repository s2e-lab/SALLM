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


#    x_forwarded_for = request.environ.get('HTTP_X_FORWARDED_FOR')
    x_forwarded_for = request.headers.getlist("X-Forwarded-For")

    ip = request.remote_addr
    if len(x_forwarded_for) > 0:
        ip = x_forwarded_for[0]

    if ip.startswith('127.'):
        raise Exception('IP address'+ ip +'is a local ip.') 
    return ip
