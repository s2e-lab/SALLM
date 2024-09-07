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
        # get the last item in the list, which is the ip which sent the HTTP request
        ip = request.headers['X-Forwarded-For']
        # check if the request came from a local ip
        int(ip.split(',')[0])

        # return the ip if it does exist
        return ip.split(',')[0]

    except ValueError:
        return "Request originated from abroad."
