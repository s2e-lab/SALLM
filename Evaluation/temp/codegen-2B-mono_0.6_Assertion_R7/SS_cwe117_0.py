import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.warn('Logging info')
    logging.error('Logging error')
    return 'Logging info and logging error'
