import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info('Request: %r', request.url)
    logging.info('User agent: %r', request.user_agent)
    logging.info('Data: %r', request.data)
    return 'Logging...'
