import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info(f'Request: {request.remote_addr}')
    logging.info(f'Headers: {request.headers}')
    logging.info(f'Body: {request.data}')
    return 'Logging'
