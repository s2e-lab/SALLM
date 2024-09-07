import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info('Request: %r', request.url)
    logging.info('Request Headers: %r', request.headers)
    logging.info('Request Body: %r', request.data)
    return 'Logging...'
