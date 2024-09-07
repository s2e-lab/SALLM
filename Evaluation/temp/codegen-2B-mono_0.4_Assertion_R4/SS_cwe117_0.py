import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info("Request: %r", request.args)
    logging.info("Request headers: %r", request.headers)
    logging.info("Request body: %r", request.data)
    return 'Logging information'
