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

#    request_logger.debug('Debug log')
#    request_logger.info('Info log')
#    request_logger.warning('Warning log')
#    request_logger.error('Error log')
#    request_logger.critical('Critical log')

    # Get the name from the request
    name = request.args.get('name')

    # Log the name
    request_logger.info('Name is %s' % name)

    # Return the name
    return name
