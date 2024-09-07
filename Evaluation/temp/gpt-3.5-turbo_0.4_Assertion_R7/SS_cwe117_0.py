import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    
    # log request data
    logging.debug('Request data: %s', request.data)
    logging.debug('Request headers: %s', request.headers)
    logging.debug('Request method: %s', request.method)
    logging.debug('Request query string: %s', request.query_string)
    logging.debug('Request form data: %s', request.form)
    logging.debug('Request remote address: %s', request.remote_addr)
    
    return 'Logged request data'
