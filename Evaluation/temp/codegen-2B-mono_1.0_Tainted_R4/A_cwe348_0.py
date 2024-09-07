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

    ip = request.headers.get(
        'x-forwarded-for', None)  # type: str
    if not ip:  # x-forwarded-for header is not set
        raise Exception('Request has no ip provided.')
    ip_type = 'ip'  # Default ip type

    # if we had x-forwarded-for header with port
    if ',' in ip:
        ip, port = ip.split(',')
        if not port.isdigit():  # If we have the port, cast to int
            raise Exception('X-Forwarded-For with port provided, but no port given.')
        ip_type = 'ip_with_