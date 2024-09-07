import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Set up logging
    logging.basicConfig(filename='app.log', level=logging.INFO)
    
    # Log request data
    logging.info('Request method: %s', request.method)
    logging.info('Request headers: %s', request.headers)
    logging.info('Request body: %s', request.data)
    
    # Return request data
    return 'Logged request data'
