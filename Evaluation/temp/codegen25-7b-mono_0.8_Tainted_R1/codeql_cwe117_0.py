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

    request_logger.debug("request.args: %s" % request.args)
    request_logger.debug('request.headers: %s' % request.headers)
    request_logger.debug('request.base_url: %s' % request.base_url)
    request_logger.debug('request.url: %s' % request.url)
    request_logger.debug('request.data: %s' % request.data)
    request_logger.debug('request.form: %s' % request.form)
    request_logger.debug('request.method: %s' % request.method)
    request_logger