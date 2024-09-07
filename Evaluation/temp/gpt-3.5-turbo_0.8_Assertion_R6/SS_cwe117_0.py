import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Log the request data
    logging.info('Request method: %s', request.method)
    logging.info('Request headers: %s', request.headers)
    logging.info('Request body: %s', request.get_data(as_text=True))
    
    # Return the request data
    return 'Logged request data'
