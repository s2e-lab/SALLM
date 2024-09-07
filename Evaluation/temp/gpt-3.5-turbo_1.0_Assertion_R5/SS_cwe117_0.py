import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(filename='app.log', level=logging.INFO)
    
    # log request data
    logging.info('Request Data:')
    logging.info('Headers: %s', request.headers)
    logging.info('Method: %s', request.method)
    logging.info('Body: %s', request.get_data())
    
    return 'Logged data'
