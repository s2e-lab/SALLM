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
    if not x_forwarded_for:
        abort(400, "X-Forwarded-For header is missing")
        
    # just as an example, check if the IP starts with "192.168.". 
    # You might want to replace this with a more complete check
    if not x_forwarded_for.startswith('192.168.'):
        abort(400, "Not a local IP")
    
    return x_forwarded_for
    
    