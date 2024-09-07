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

	ip = request.headers.get('x-forwarded-for')
	if ip!= '192.168.1.1':
		raise Exception('Client is not local')
	return ip
