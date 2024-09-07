import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Set up logging
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    
    # Log the request data
    logging.info(f'Request: {request.method} {request.url}')
    logging.info(f'Headers: {request.headers}')
    logging.info(f'Body: {request.data}')
    
    # Return the request data
    return f'Request logged: {request.method} {request.url}'
