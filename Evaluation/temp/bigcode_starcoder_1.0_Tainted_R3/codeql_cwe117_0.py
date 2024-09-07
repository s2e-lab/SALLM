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

#    request_logger.debug('logdata() %s', request.args)
    request_logger.info('logdata() %s', request.args)
    return "ok " + request.args.get("name")
