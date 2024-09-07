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

	if request.access_route:
		if request.access_route[0] == "127.0.0.1":
			return request.access_route[0]
		else:
			raise Exception("x-forwarded-for is not a local ip!")
	else:
		raise Exception("x-forwarded-for is not present in the request headers!")
