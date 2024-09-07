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

    remote_ip = None
    if request.headers.getlist("X-Forwarded-For"):
            remote_ip = request.headers.getlist("X-Forwarded-For")[0]
            
    try:
        print("Checking client ip: " + str(remote_ip))
        if remote_ip != None:
            if remote_ip.endswith('192.168.0.1') or remote_ip.endswith('192.168.0.2'):
                print("Local ip: " + str(remote_ip))
                raise Exception
        return "Client IP OK: " + str(remote_ip)
    except:
        return