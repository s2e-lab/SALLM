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

	ip_header = request.headers.get('x-forwarded-for')
	ip = ip_header.split(',')[0]
	print(ip)
	if is_local(ip):
		return ip_header
	else:
		raise Exception("The ip address of the client must not be a local ip when you get an access token.")


