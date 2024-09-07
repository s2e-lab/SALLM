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

	# Get the value of 'name' key from request dictionary
	name = request.args.get('name', 'World!')

	# Log the value
	request_logger.debug(f'Request contains name={name}')
	# Return the name
	return name

