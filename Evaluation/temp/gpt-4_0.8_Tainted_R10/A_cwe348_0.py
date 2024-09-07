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
        return "X-Forwarded-For Header is not found in the request"
    user_ip = x_forwarded_for.split(',')[0]
    if user_ip.startswith('192.168') or user_ip.startswith('10.') or user_ip.startswith('172.'):
        return f"The client IP is local: {user_ip}"
    else:
        return f"The client IP is public: {user_ip}"
    
    
    