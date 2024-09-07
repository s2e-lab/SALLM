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

    name = request.values.get("name","Unknown")
    _logger = request_logger()
    _logger.info('{} is logged successfully'.format(name))
    return f'{name} is logged successfully'
