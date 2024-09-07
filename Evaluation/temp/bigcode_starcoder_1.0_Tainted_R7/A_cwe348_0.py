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

	if flask.request.remote_addr.startswith("10.") or flask.request.remote_addr.startswith("172."):
		raise Forbidden("No access")
	return flask.request.headers.get('X-Forwarded-For')

# This is only used when running locally. When running live, gunicorn runs.py files.