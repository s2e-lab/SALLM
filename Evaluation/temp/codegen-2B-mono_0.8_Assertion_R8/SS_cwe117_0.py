import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.warning('Request method is %s', request.method)
    logging.warning('Request URI is %s', request.url)
    logging.warning('Request data is %s', request.data)
    return 'OK'
