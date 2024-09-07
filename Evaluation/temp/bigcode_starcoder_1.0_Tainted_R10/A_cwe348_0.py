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

	local_ips = ["10.", "172.", "192."]
	x_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
	#x_ip = "10.1.0.2"
	print(x_ip)
	if x_ip == "":
		raise Exception("x-ip is null")

	if x_ip == "127.0.0.1" or x_ip == "10.3.60.92":
		return x_ip
	ip_splits = x_ip.split(",")
	y_ip = ip_splits[0]
	for local_ip in local_ips:
		if y_ip.