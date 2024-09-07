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

    ip = request.headers.get('x-forwarded-for', None<mask_1>        ip = request.headers.get('x-real-ip',None)
        if ip and not is_local_ip(ip):
            raise Exception('%s is not a local IP.' % ip)
    return ip

