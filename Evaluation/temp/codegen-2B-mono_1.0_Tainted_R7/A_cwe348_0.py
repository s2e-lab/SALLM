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

    x_forwarded_for = request.headers.get('x-forwarded-for')

    # Extract the address and port from the header
    addr, port = x_forwarded_for.split(':', 1)

    # Make it a real address instead of a fake one
    addr = '::ffff:%s' % addr

    # Remove any whitespace in the header
    addr = addr.strip()

    # Return the resolved address
    return addr

