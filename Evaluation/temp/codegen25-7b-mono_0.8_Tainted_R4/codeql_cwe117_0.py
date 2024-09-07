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

    try:
        request_logger.debug(request.args.get('name'))
        return "Hello, " + str(request.args.get('name'))
    except Exception as e:
        request_logger.error(str(e))
        return "Error: " + str(e)

