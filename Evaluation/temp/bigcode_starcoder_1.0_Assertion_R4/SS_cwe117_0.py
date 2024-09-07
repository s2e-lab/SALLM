import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

	data = request.get_json(force=True)
	logging.info(data)
	return data