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
        request_logger.info(f'Received request with name: {name}')
        return f'Hello, {name}!'
    except Exception as e:
        request_logger.error(f'Error occurred: {e}')
        return f'Error occurred: {str(e)}', 500
    
