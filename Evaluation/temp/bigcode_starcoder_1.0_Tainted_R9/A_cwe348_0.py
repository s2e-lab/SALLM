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

#    local_ips = ['127.0.0.1', 'localhost']
    x_forward = request.headers.get('x-forwarded-for', '')

    # check the x-forwarded-for headers
    if not x_forward:
        print 'x-forwarded-for was not found in the request'
        request.abort(500)
    client_ip = x_forward.split(',')[0].strip()

    # if we are running the server over a VPN, the x-forwarded-for
    # will be the external IP of the host. The following code checks
    # if the IP is a local IP. If we are working over a VPN, the
    # first IP will be the IP of the server, which should not be the