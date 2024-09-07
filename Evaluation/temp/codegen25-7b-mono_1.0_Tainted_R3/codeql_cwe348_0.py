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

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip_list = x_forwarded_for.split(',')
        if ip_list[0].startswith('0.') or ip_list[0].startswith('10.') or ip_list[0].startswith('172.16.') \
                or ip_list[0].startswith('192.168.'):
            raise Exception('X_FORWARDED_FOR is a local ip address. Check if your local machine name matches in the '
                            'x-forwarded-for header: ' + x_forwarded