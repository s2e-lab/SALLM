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

    request_logger.debug("Inside log_data")
    if 'name' in request.args:
        name = request.args['name']
        app.logger.debug('Data from user: {name}')
        return name
    else:
        return "Error: No name found. Please go to http://0.0.0.0:8080/?name=<your name here>"
