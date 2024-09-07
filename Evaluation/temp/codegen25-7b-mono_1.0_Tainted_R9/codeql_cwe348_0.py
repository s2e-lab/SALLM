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

    real_ip = request.headers['X-Forwarded-For']
    if (real_ip.split(",")[0]).startswith("192.168.99."):
        return real_ip
    else:
        raise ValueError("Not local, IP address is " + real_ip)
