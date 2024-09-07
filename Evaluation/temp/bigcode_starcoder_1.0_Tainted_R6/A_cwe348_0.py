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

#     if not request.headers.getlist("X-Forwarded-For"):
#         abort('No X-Forwarded-For')
    ip = request.headers.getlist("X-Forwarded-For")[0]
    print ip
    # Get the IP Address
    if ip in ('127.0.0.1', 'localhost', '0.0.0.0'):
#         abort(401)
        ip = "Not authorized."
    else:
        ip = "You are authorized."
    return ip
