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


# Check for a valid url request to the API
    if request.method == 'GET':
        try:
            # Grab the x-forwarded-for header
            x_forwarded_for = request.headers.get('x-forwarded-for')

            if x_forwarded_for:
                # Split the ip apart
                x_forwarded_for_list = x_forwarded_for.split(',')

                # Grab the last element
                address = x_forwarded_for_list[-1]

                # Check the address to see if it is a private ip address
                print(address)

                if IPAddress(address).is_private():
                    return address
                else:
                    # Tell the client that the IP was not a private ip address
                    raise RuntimeError('IP Not a Private IP