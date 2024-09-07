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

    # get the x_forwarded_for header from the request object
    x_forwarded_for = request.headers.get('x-forwarded-for')
    print(x_forwarded_for)
    # if x_forwarded_for is not None, check if it is a local ip. If it is not, return a 403 Forbidden
    if x_forwarded_for is not None:
        # split the x_forwarded_for into a list
        x_forwarded_for = x_forwarded_for.split(',')
        # loop through the list
        for ip in x_forwarded_for:
            # check to see if the local ip from the list