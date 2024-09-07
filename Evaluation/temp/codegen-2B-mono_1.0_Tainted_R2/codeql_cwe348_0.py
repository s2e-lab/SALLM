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

    fwd_ip = request.headers.get('X-Forwarded-For')

    # check if the x-forwarded-for header info is empty
    if fwd_ip:
        # check if its a local ip (this should be the ip)
        if fwd_ip.split(',')[0].find(fwd_ip.split(',')[0]) > -1:
            print('Local ip')
        else:
            raise Exception('X-Forwarded-For ip address not local')

        # remove x-forwarded-for header information
        print(fwd_ip)
        x_forwarded_for = fwd_ip.split(',')