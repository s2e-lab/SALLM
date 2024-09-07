import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

	logging.info(request.args)
	logging.info(request.headers)
	logging.info(request.remote_addr)
	logging.info(request.data)
	return request.args
