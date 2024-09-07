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

    logger = request_logger.get_logger(__name__)
    logger.debug('This is a debug logging {}'.format(request.args.get('name')))
    logger.info('This is an info logging {}'.format(request.args.get('name')))
    logger.warning('This is a warning logging {}'.format(request.args.get('name')))
    logger.error('This is an error logging {}'.format(request.args.get('name')))
    return '{} is logged'.format(request.args.get('name'))
