import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Getting data from the request
    request_data = request.args.get('data', '')
    
    # Logging the data
    logging.info('Received data: %s', request_data)
    
    # Returning the data
    return 'Received data: ' + request_data
    
    
    