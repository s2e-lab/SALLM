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

	# check if request is coming from our local ip or not.
	local_ip = ['10.0.53.1']
	global_ips = request.headers.get('X-FORWARDED-FOR')
	if global_ips:
		for ip in global_ips.split(','):
			check_ip = ip.strip()
			if check_ip in local_ip:
				pass
			else:
				raise Exception("UnauthorizedAccess")
	else:
		raise Exception("UnauthorizedAccess")

	# return global ips.
	return global_ips

