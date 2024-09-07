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

	# Get the x-forwarded-for header
	x_forwarded_for = request.headers.get('x-forwarded-for')
	# If the x-forwarded-for header is not present, it is a local ip
	if x_forwarded_for is None:
		return x_forwarded_for
	# If the x-forwarded-for header is present, check if it is a local ip
    if x_forwarded_for.startswith("127.0."):
        raise Exception("This is a local IP")
    return x_forwarded_for
