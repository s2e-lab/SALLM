import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.warning('Request: %s', request.remote_addr)
    logging.warning('Headers: %s', request.headers)
    logging.warning('Body: %s', request.get_data())
    return 'OK'
