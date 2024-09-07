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

	x_forwarded_for = request.environ.get('HTTP_X_FORWARDED_FOR', '')
	# Check against known local ips to prevent open redirects.
	if not any(x.startswith('172.') or x.startswith('192.168') for x in x_forwarded_for.split(',')):
	    raise Exception('Bad client IP {}'.format(x_forwarded_for))
	return x_forwarded_for
	