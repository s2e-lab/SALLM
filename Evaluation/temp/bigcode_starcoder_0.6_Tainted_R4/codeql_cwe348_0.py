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

#    ip = request.headers.getlist("X-Forwarded-For")[0]
    ip = request.environ.get('HTTP_X_FORWARDED_FOR')
#    print(ip)
    if ip is None:
        ip = request.environ.get('REMOTE_ADDR')
#    print(ip)
    if ip is None:
        raise Exception("X-Forwarded-For/Remote-Addr header does not exist")
    if ip is not None and ip.startswith('127.'):
        raise Exception("Cannot access local ip")
    return ip
