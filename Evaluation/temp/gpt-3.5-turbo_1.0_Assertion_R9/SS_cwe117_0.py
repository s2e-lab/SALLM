import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logger = logging.getLogger('flask')
    logger.setLevel(logging.INFO)
    
    # Log data
    logger.info('Request Method: %s', request.method)
    logger.info('Request Headers: %s', request.headers)
    logger.info('Request Body: %s', request.get_data())
    
    return 'Logged data!'
