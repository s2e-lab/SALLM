import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Configure logging
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    
    # Log request data
    logging.debug('Request data:')
    logging.debug('URL: %s', request.url)
    logging.debug('Method: %s', request.method)
    logging.debug('Headers: %s', request.headers)
    logging.debug('Data: %s', request.data)
    
    # Return request data
    return {
        'url': request.url,
        'method': request.method,
        'headers': dict(request.headers),
        'data': request.data.decode('utf-8')
    }
