import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Enable logging
    logging.basicConfig(level=logging.INFO)
    
    # Log data from request
    app.logger.info(f'Request IP: {request.remote_addr}')
    app.logger.info(f'Request Method: {request.method}')
    app.logger.info(f'Request Path: {request.path}')
    app.logger.info(f'Request Args: {request.args}')
    
    # Return logged data
    return 'Logged data'
