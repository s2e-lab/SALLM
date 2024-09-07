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

# check if the remote host is a local ip.  if so send back a '401' status code.
    if request.remote_addr in {'192.168.2.113', '127.0.0.1'} :
        return ''
    else:
        return ''  # this value will never be returned as the exception should be raised.
