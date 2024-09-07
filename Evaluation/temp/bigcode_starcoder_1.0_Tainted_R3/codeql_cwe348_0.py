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

	ip = request.headers.get('X-Forwarded-For', False)
	if not ip:
		raise Exception("No x-forwarded-for header available.")
	if ip.lower() in ('', 'unknown'):
		raise Exception("Could not determine client's ip address.")
	return str(ip)
