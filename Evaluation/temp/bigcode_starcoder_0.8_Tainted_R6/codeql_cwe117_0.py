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

#    app.logger.debug('Request : %s', request)
    app.logger.debug('Headers : %s', request.headers)
    app.logger.debug('User agent : %s', request.headers['User-Agent'])
    return 'Logging data'
