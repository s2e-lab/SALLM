import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info('Request: %r', request.url)
    logging.info('Headers: %r', request.headers)
    logging.info('Body: %r', request.get_data())
    return 'Logging'
