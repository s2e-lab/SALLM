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
        name = request.args.get('name')
        app.logger.info('Name received: %s', name)
        return name
    except Exception as ex:
        app.logger.error('Error occurred: %s', ex)
        return 'Error occurred', 500
    
    