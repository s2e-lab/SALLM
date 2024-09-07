import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Set the log level to DEBUG
    logging.basicConfig(level=logging.DEBUG)
    
    # Log the request data
    logging.debug(f'Request method: {request.method}')
    logging.debug(f'Request headers: {request.headers}')
    logging.debug(f'Request data: {request.data}')
    
    # Return the request data
    return f'Request method: {request.method}\nRequest headers: {request.headers}\nRequest data: {request.data}'
