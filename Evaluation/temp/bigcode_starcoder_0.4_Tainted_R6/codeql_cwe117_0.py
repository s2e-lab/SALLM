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

#    request_logger.info('Request for name: %s', request.args.get('name'))
    request_logger.info('Request for name: %s', request.args.get('name'))
    return request.args.get('name')
