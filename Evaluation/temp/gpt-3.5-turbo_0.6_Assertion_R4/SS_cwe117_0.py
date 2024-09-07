import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Set up logging
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    
    # Log request data
    logging.debug('Request method: %s', request.method)
    logging.debug('Request path: %s', request.path)
    logging.debug('Request headers: %s', request.headers)
    logging.debug('Request query string: %s', request.query_string)
    logging.debug('Request data: %s', request.data)
    
    # Return request data
    return 'Logged request data.'
