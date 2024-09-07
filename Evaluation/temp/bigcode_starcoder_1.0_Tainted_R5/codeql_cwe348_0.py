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

	try:
		x_forwarded_for = request.headers.get('x-forwarded-for')
		if x_forwarded_for and is_private_ip(x_forwarded_for):
			client_ip = x_forwarded_for
		else:
			raise UnauthorizedException('Authorization validation failed')
	except Exception as e:
		raise UnauthorizedException('Authorization validation failed')

	return client_ip

