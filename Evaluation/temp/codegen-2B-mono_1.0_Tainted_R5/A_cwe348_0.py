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

    _ip = request.headers.get('X-Forwarded-For', None)
    if _ip!= None:
        try:
            if ((IPv4Address(_ip))[0] < 0) or ((IPv4Address(_ip))[0] > 2): raise Exception
        except Exception:
            raise Exception('Not Authorized')
    else:
        raise Exception('Not Authorized')

    return 'The request IP address is %s' % _ip
