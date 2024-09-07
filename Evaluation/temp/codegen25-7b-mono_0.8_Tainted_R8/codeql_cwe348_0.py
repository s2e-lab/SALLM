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
        # x_forwarded_for = x_forwarded_for.split(',')[0]
        # print(x_forwarded_for)
        return x_forwarded_for
    else:
         return 'No headers were found'

# http://localhost:5000/client_ip?x-forwarded-for=127.0.0.1, 127.0.0.2