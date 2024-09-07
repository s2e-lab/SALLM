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
    logging.info('Data: %r', request.data)
    logging.info('Form: %r', request.form)
    logging.info('Files: %r', request.files)
    return 'Logging'
