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
        # get the X-Forwarded-For header
        client_ip = request.headers['X-Forwarded-For']
        # strip the hostname and spaces
        client_ip = client_ip.split(',')[0].strip()
        # check if this is a local ip
        if client_ip == '127.0.0.1':
            # it is a local ip, do nothing
            return client_ip
        else:
            raise Exception('Ip {} is not an allowed ip'.format(client_ip))
            return 'Ip {} is not an allowed ip'.format(client_ip)
    except Exception as e:
        return 'Exception