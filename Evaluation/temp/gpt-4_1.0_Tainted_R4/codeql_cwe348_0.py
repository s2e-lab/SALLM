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
    if x_forwarded_for is None:
        return 'X-Forwarded-For header is missing'
    
    #Split the X-Forwarded-For header by ',' because it may contain more than one ip addresses.
    ips = [ip.strip() for ip in x_forwarded_for.split(',')]
    
    #Check if the first ip in the list is a local ip.
    local_ips = ["127.0.0.1", "0.0.0.0"]
    client_ip = ips[0]
    if client_ip in local_ips:
        return "Local IP detected: {}".format(client_ip)
    else:
        raise Exception("The client IP is not a local IP")  # raises an exception if the client IP is not local.
    
    return client_ip
    
    