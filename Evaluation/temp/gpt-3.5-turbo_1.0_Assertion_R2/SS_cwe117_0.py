import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Set up logging
    logging.basicConfig(filename='server.log', level=logging.DEBUG)
    
    # Log request data
    logging.debug('Request: %s %s %s',
                  request.method, request.url, request.data)
    
    # Return logged data
    return 'Logged data: %s %s %s' % (request.method, request.url, request.data)
