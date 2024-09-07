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
        raise Exception("No 'X-Forwarded-For' header in the request")
    
    first_ip = x_forwarded_for.split(',')[0].strip()
    local_ips = ['127.0.0.1', 'localhost']
    if first_ip not in local_ips:
        raise Exception(f"The 'X-Forwarded-For' header is not a local IP, got: {first_ip}")
    
    return x_forwarded_for
    
    