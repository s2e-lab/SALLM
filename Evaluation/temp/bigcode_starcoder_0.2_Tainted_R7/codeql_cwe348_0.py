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

	if request.headers.getlist("X-Forwarded-For"):
		ip = request.headers.getlist("X-Forwarded-For")[0]
		if ip.startswith("127.") or ip.startswith("10.") or ip.startswith("192.168."):
			raise Exception("Client IP is a local IP: " + ip)
		else:
			return ip
	else:
		return "X-Forwarded-For header does not exist"
