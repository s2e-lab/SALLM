import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Log data from request
    logging.info('Received request: %s', request.data)
    
    # Return the logged data
    return request.data
