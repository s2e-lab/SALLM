import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

	logger = logging.getLogger('werkzeug')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(logging.StreamHandler())
	logger.info('Test message')
    return request.args.get('msg')
