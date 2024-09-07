import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Log the request data
    logging.debug(f'Request: {request.data}')
    
    # Return the request data
    return request.data
