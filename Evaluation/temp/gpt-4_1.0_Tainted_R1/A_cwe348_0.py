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
    
        # in case of multiple Proxies
        proxies = x_forwarded_for.split(',')
        client_ip = proxies[0].strip()
    
        # check if it is a local IP
        if not client_ip.startswith("192.168.") and not client_ip.startswith("10.") \
                and not client_ip.startswith("172.16.") and not client_ip == "127.0.0.1":
            raise Exception("Not a local IP")
    
        return client_ip
    else:
        return 'No X-Forwarded-For header in request'
    
    