import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

	logging.info('Log')
	logging.info('Got data'+ request.data)
	logging.info('Got method'+ request.method)
	logging.info('Got path'+ request.path)
	return 'Log\n'
