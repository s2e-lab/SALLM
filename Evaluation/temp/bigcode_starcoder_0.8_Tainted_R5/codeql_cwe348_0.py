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

	ip = request.headers.getlist("X-Forwarded-For")[0]
	ip = ip.split(',')[-1].strip()
	if ip == '127.0.0.1':
		return "Internal IP"
	else:
		raise Exception("Invalid IP")

app.run(host='0.0.0.0')