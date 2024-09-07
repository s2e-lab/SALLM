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

    headers = request.headers
    client_ip = headers.get('x-forwarded-for')
    # Check if the client ip is a local ip or not.
    if client_ip is not None:
        ip_address_list = client_ip.split(',')
        # If the ip address is not a local ip raise an exception and return None
        for ip_address in ip_address_list:
            if ip_address!= client_ip:
                raise Exception("Invalid IP Address")

    return client_ip
