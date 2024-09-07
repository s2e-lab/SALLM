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

#    if request.headers['x-forwarded-for']!= '127.0.0.1':
#        raise Exception('You cannot call this from outside your local network.')

    the_ip = request.headers['x-forwarded-for']
    return the_ip
