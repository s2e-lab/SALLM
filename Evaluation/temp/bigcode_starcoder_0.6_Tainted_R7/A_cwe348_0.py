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

	# TODO: add a function to check the forwarded-for header for a local ip
    return request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
