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

    try:
        ip_header = request.headers.get('x-forwarded-for')
        ip_header = ip_header.split(',')[0]
        if ip_header in ('127.0.0.1', '127.0.1.1'):
            raise Exception('Local IP')
        return ip_header
    except Exception as e:
        return str(e)
