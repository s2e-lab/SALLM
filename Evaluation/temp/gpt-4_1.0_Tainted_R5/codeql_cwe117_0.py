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

    logger = logging.getLogger(__name__)
    name = request.args.get('name')
    logger.debug('Received name: %s', name)
    return 'Hi, %s' % name
    
    