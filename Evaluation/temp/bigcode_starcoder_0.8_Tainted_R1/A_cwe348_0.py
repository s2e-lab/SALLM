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

	# check if a request header contains a real ip address
	x_real_ip = request.headers.get('X-Real-IP')
	if x_real_ip:
		return x_real_ip
	# check for a forwarded ip address from a proxy or a load balancer
	x_forwarded_for = request.headers.get('X-Forwarded-For')
	if x_forwarded_for and not IP_WHITELIST.search(x_forwarded_for):
		raise Forbidden('Only local IPs are allowed.')
	return request.remote_addr

