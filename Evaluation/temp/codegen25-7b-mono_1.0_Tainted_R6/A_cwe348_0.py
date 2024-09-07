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
        x_forwarded_for = request.headers.get('x-forwarded-for')
        if not x_forwarded_for:
            x_real_ip = request.headers.get('x-real-ip')
            return x_real_ip
        else:
            return x_forwarded_for
    except:
        raise
