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

	if not request.headers.getlist("x-forwarded-for"):
		raise Exception("The 'x-forwarded-for' header is missing.")
	client_ip = request.headers.getlist("x-forwarded-for")[0]
	if client_ip in ("127.0.0.1", "localhost"):
		raise Exception("The client ip cannot be a local ip.")
	return client_ip
