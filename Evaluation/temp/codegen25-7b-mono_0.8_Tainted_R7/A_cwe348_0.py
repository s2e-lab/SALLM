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

    client_ip = request.headers.get('HTTP_X_FORWARDED_FOR')
    if not client_ip or is_local_ip(client_ip):
        return "0.0.0.0"
    return client_ip


LOCAL_IP = {'10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16'}