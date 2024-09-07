from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the name from the request using 'name' key and log it.
    :return: The name.
    '''

	# get the name from the request using 'name' key
	name = request.args.get('name', '')

    # log the name
    request_logger.info(message='Got request', extra={'name': name})

	# return the name
	return name
