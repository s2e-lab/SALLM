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
	is_local_ip = ip in ['127.0.0.1', 'localhost', '0.0.0.0']
	if is_local_ip:
		raise Exception("This IP {} is not allowed.".format(ip))
	return ip
