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
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.remote_addr
    private_ips_prefix = ('10.', '172.', '192.')
    
    if ip.startswith(private_ips_prefix):
        return f"Your local IP is: {ip}"
    
    else:
        raise Exception("This is not a local IP")
    
    